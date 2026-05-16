import openai
import json
import asyncio

from config.config import GENERATOR_MAX_TOKENS

class QuestionGenerator:
    def __init__(self, api_key, api_base, model):
        self.client = openai.AsyncOpenAI(api_key=api_key, base_url=api_base)
        self.model = model
        self.generation_lock = asyncio.Lock() # To prevent multiple concurrent generations

    async def generate_questions(self, exam_tag, existing_questions_context=None, num_questions=5):
        async with self.generation_lock:
            print(f"Generating {num_questions} questions for {exam_tag}...")
            prompt = self._build_prompt(exam_tag, existing_questions_context, num_questions)
            
            try:
                chat_completion = await self.client.chat.completions.create(
                    messages=[
                        {"role": "system", "content": "You are an expert in Microsoft 365 exams, specifically for the " + exam_tag.upper() + " certification. Generate new, unique, and challenging multiple-choice questions with explanations."},
                        {"role": "user", "content": prompt}
                    ],
                    model=self.model,
                    response_format={"type": "text"},
                    temperature=0.7,
                    max_tokens=GENERATOR_MAX_TOKENS # Increased to prevent truncation of multiple detailed questions
                )
                
                response_content = chat_completion.choices[0].message.content
                
                # Clean markdown code blocks if present (common with local LLMs in text mode)
                cleaned_content = response_content.strip()
                if cleaned_content.startswith("```"):
                    lines = cleaned_content.splitlines()
                    # Remove the first line (```json)
                    cleaned_content = "\n".join(lines[1:])
                    # Remove the last line only if it's the closing backticks
                    if cleaned_content.strip().endswith("```"):
                        cleaned_content = "\n".join(cleaned_content.strip().splitlines()[:-1])
                
                generated_data = json.loads(cleaned_content)
                
                if "questions" in generated_data:
                    print(f"Successfully generated {len(generated_data['questions'])} questions.")
                    return generated_data["questions"]
                else:
                    print("LLM response did not contain 'questions' key.")
                    return []
            except openai.APIError as e:
                print(f"OpenAI API Error: {e}")
                return []
            except json.JSONDecodeError as e:
                print(f"JSON Decode Error from LLM response: {e}")
                print(f"Raw LLM response: {response_content}")
                return []
            except Exception as e:
                print(f"An unexpected error occurred during question generation: {e}")
                return []

    def _build_prompt(self, exam_tag, existing_questions_context, num_questions):
        prompt = f"Generate exactly {num_questions} new, unique, and challenging multiple-choice questions for the {exam_tag.upper()} Microsoft certification exam. Each question should have 4 options, a single correct answer (0-indexed), and a detailed explanation. The questions should cover diverse topics relevant to the exam. Ensure the output is a JSON object with a single key 'questions' which is a list of question objects. Each question object must have 'q', 'options' (list of strings), 'answer' (integer), and 'explanation' (string) keys.\n\n"
        
        if existing_questions_context:
            # Provide some context to avoid generating similar questions
            # Limit context size to avoid exceeding token limits
            context_str = json.dumps(existing_questions_context[:5]) # Use first 5 questions as context
            prompt += f"Avoid generating questions similar to these recent ones:\n{context_str}\n\n"
        
        prompt += "Example format for one question:\n"
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