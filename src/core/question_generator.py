import openai
import json
import asyncio
import re

from config.config import GENERATOR_MAX_TOKENS, MAX_GENERATION_RETRIES

class QuestionGenerator:
    def __init__(self, api_key, api_base, model):
        self.client = openai.AsyncOpenAI(api_key=api_key, base_url=api_base)
        self.model = model
        self.generation_lock = asyncio.Lock() # To prevent multiple concurrent generations

    async def generate_questions(self, exam_tag, existing_questions_context=None, num_questions=7):
        async with self.generation_lock:
            print(f"Generating {num_questions} questions for {exam_tag}...")
            user_prompt = self._build_prompt(exam_tag, existing_questions_context, num_questions)
            
            messages = [
                {
                    "role": "system", 
                    "content": (
                        f"You are an expert in the {exam_tag.upper()} certification. "
                        f"Your task is to generate {num_questions} new, unique, relevant, diverse and very challenging"
                        " multiple-choice questions with explanations in strict JSON format. "
                        f"CRITICAL: The output must be a SINGLE JSON object with exactly one key named 'questions' "
                        f"containing EXACTLY {num_questions} question objects. "
                        "Do NOT include trailing commas after the last element in an array or object. "
                        "Ensure every object in an array is separated by a comma. "
                        "Provide ONLY the raw JSON content."
                    )
                },
                {"role": "user", "content": user_prompt}
            ]
            
            for attempt in range(MAX_GENERATION_RETRIES):
                try:
                    chat_completion = await self.client.chat.completions.create(
                        messages=messages,
                        model=self.model,
                        response_format={"type": "text"},
                        temperature=0.7,
                        max_tokens=GENERATOR_MAX_TOKENS
                    )
                    
                    response_content = chat_completion.choices[0].message.content
                    sanitized_content = self._sanitize_json(response_content)
                    
                    try:
                        generated_data = json.loads(sanitized_content)
                        
                        if "questions" in generated_data and isinstance(generated_data["questions"], list):
                            actual_count = len(generated_data["questions"])
                            if actual_count == num_questions:
                                print(f"Successfully generated {actual_count} questions on attempt {attempt + 1}.")
                                return generated_data["questions"]
                            else:
                                print(f"Discarding incomplete generation on attempt {attempt + 1}: found {actual_count}, expected {num_questions}. Skipping to next attempt.")
                                # We do not add the incomplete response to the conversation history
                                # to prevent the model from thinking partial data is acceptable.
                                continue
                        else:
                            raise ValueError("Missing 'questions' key or invalid format.")
                            
                    except (json.JSONDecodeError, ValueError) as e:
                        print(f"Attempt {attempt + 1} failed to parse JSON: {e}")
                        # Feedback loop: Send the error back to the LLM
                        messages.append({"role": "assistant", "content": response_content})
                        messages.append({
                            "role": "user", 
                            "content": f"Your previous response had a JSON error: {str(e)}. Please provide the corrected, full JSON object now, containing ALL {num_questions} questions. Ensure no trailing commas and proper comma separation."
                        })
                        continue

                except openai.APIError as e:
                    print(f"OpenAI API Error: {e}")
                    return []
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                    return []
            
            print(f"Failed to generate valid JSON after {MAX_GENERATION_RETRIES} attempts.")
            return []

    async def distill_questions(self, questions_batch, num_per_block=7):
        """Meticulously filters and refines a batch of questions to remove repetition and fluff."""
        async with self.generation_lock:
            print(f"Distilling {len(questions_batch)} questions...")
            
            prompt = (
                f"You are a world-class certification editor. Below is a list of practice questions for {self.model.upper()}. "
                "Your goal is to perform 'Question Distillation':\n"
                "1. REMOVE REPETITION: Many concepts repeat across sections. Identify and remove near-duplicate questions.\n"
                "2. FILTER FLUFF: Remove low-quality or overly simple questions.\n"
                "3. REPAIR BROKEN DATA: Meticulously check for and fix 'broken' questions:\n"
                "   - Identify and repair questions with empty, null, or incorrect answer mappings.\n"
                "   - Clarify or remove vague, ambiguous, or nonsensical questions.\n"
                "   - Verify that the 'answer' index correctly points to the factually accurate option.\n"
                "   - Enrich empty or generic explanations with technical depth.\n"
                "4. ENHANCE DEPTH: Keep only the most complex, unique, and diverse questions.\n"
                f"5. VOLUME: Aim to preserve as many high-quality questions as possible. Do not delete unique technical content.\n"
                f"6. STRUCTURE: Group the result into blocks of EXACTLY {num_per_block}.\n\n"
                "Output ONLY raw JSON in this format: {\"distilled_sections\": {\"Distilled Block 1\": [questions], ...}}\n\n"
                f"DATA TO DISTILL:\n{json.dumps(questions_batch)}"
            )

            messages = [
                {"role": "system", "content": "You are a world-class certification editor. You always respond with valid, complete JSON."},
                {"role": "user", "content": prompt}
            ]

            for attempt in range(MAX_GENERATION_RETRIES):
                try:
                    completion = await self.client.chat.completions.create(
                        messages=messages,
                        model=self.model,
                        response_format={"type": "text"},
                        temperature=0.2, # Extremely low temperature for structural integrity
                        max_tokens=GENERATOR_MAX_TOKENS
                    )
                    
                    response_content = completion.choices[0].message.content
                    if not response_content or response_content.strip() == "":
                        raise ValueError("Empty response from LLM")

                    sanitized_content = self._sanitize_json(response_content)
                    response = json.loads(sanitized_content)
                    
                    distilled = response.get("distilled_sections", {})
                    if distilled:
                        return distilled
                    
                    raise ValueError("JSON parsed but 'distilled_sections' key was missing or empty.")

                except (json.JSONDecodeError, ValueError, Exception) as e:
                    print(f"Distillation attempt {attempt + 1} failed: {e}")
                    if attempt == MAX_GENERATION_RETRIES - 1:
                        return {}
                    await asyncio.sleep(2) # Brief backoff

    def _sanitize_json(self, content):
        """Attempts to fix common LLM JSON formatting errors."""
        # 1. Remove markdown code blocks
        cleaned = content.strip()
        if "```" in cleaned:
            # Extract content between ```json and ``` or just ```
            match = re.search(r"```(?:json)?\s*(.*?)\s*```", cleaned, re.DOTALL)
            if match:
                cleaned = match.group(1)
            else:
                # Fallback: remove lines starting with ```
                cleaned = "\n".join([line for line in cleaned.splitlines() if not line.strip().startswith("```")])

        # 2. Remove trailing commas before closing braces/brackets
        cleaned = re.sub(r",\s*([\]}])", r"\1", cleaned)
        
        # 3. Fix missing commas between objects/arrays (e.g., } { or ] {)
        cleaned = re.sub(r"}\s*{", "}, {", cleaned)
        cleaned = re.sub(r"\]\s*{", "], {", cleaned)
        
        return cleaned.strip()

    def _build_prompt(self, exam_tag, existing_questions_context, num_questions):
        prompt = f"Generate exactly {num_questions} new, unique, and challenging multiple-choice questions for the {exam_tag.upper()} certification. Each question must have 4 options, a single correct answer (0-indexed), and a detailed explanation. Cover diverse topics.\n\n"
        prompt += f"Requirements:\n- Output a SINGLE JSON object containing EXACTLY {num_questions} questions.\n- Use a SINGLE key named 'questions'.\n- Do NOT repeat the 'questions' key; all questions must be in one list.\n- Ensure NO trailing commas.\n\n"
        
        if existing_questions_context:
            context_str = json.dumps(existing_questions_context[:5]) # Use first 5 questions as context
            prompt += f"Avoid generating questions similar to these recent ones:\n{context_str}\n\n"
        
        prompt += "Expected JSON structure:\n"
        prompt += """{
            "questions": [
                {
                    "q": "What is the primary purpose of Microsoft Entra ID?",
                    "options": ["File storage", "Identity and access management", "Email hosting", "Project management"],
                    "answer": 1,
                    "explanation": "Microsoft Entra ID (formerly Azure AD) is Microsoft's cloud-based identity and access management service."
                }
            ]
        }"""
        return prompt