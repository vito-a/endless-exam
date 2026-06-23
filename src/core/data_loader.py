import os
import importlib.util
import random
import json
from pathlib import Path
import asyncio # Keep asyncio for the async generation loop
import time
from config.config import OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_MODEL, NUM_QUESTIONS_TO_GENERATE
from src.core.question_generator import QuestionGenerator

class DataManager:
    @staticmethod
    def discover_exams(data_dir="data"):
        """Scans the data directory for all valid python exam modules."""
        exams = []
        project_root = Path.cwd().resolve()
        base_path = (project_root / data_dir).resolve()
        
        for py_file in base_path.rglob("*.py"):
            if py_file.name == "__init__.py": continue
            
            # Create a module name from path
            rel_path = py_file.relative_to(project_root) # Calculate relative path from current working directory
            module_name = str(rel_path).replace(os.sep, ".").replace(".py", "")
            
            try:
                spec = importlib.util.spec_from_file_location(module_name, py_file)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, 'PRACTICE_DATA'):
                    exams.append({
                        "tag": getattr(module, "EXAM_TAG", py_file.stem),
                        "title": getattr(module, "EXAM_TITLE", py_file.stem),
                        "module_path": module_name,
                        "file_path": str(py_file),
                        "data": module.PRACTICE_DATA
                    })
            except Exception as e:
                print(f"Error loading {py_file}: {e}")
        
        return exams

    @staticmethod
    def get_randomized_exam(exam_list, target_count=70):
        """Pools questions from multiple exams and randomizes them."""
        pool = []
        for exam in exam_list:
            for section in exam["data"].values():
                pool.extend(section)
        
        selected = random.sample(pool, min(target_count, len(pool)))
        
        # Re-package into blocks of 7
        master_data = {}
        block_size = 7
        for i in range(0, len(selected), block_size):
            block = selected[i:i + block_size]
            master_data[f"Random Block {i//block_size + 1}"] = block
            
        return master_data

    @staticmethod
    def export_to_json(output_dir="src/web/static/data"): # Default output directory for web assets
        """Exports all python data to JSON for pure HTML/JS usage (github.io)."""
        os.makedirs(output_dir, exist_ok=True)
        exams = DataManager.discover_exams()
        
        manifest = []
        for exam in exams:
            filename = f"{exam['tag']}.json"
            with open(os.path.join(output_dir, filename), "w") as f:
                json.dump(exam['data'], f)
            
            manifest.append({
                "tag": exam["tag"],
                "title": exam["title"],
                "file": filename
            })
            
        with open(os.path.join(output_dir, "manifest.json"), "w") as f:
            json.dump(manifest, f)
        return output_dir

    @staticmethod
    def get_endless_exam_file_path(exam_tag):
        """Constructs the path to the endless exam file for a given tag."""
        endless_dir = Path("data") / exam_tag
        endless_dir.mkdir(parents=True, exist_ok=True)
        return endless_dir / f"{exam_tag}_endless.py"

    @staticmethod
    def load_endless_exam_data(exam_tag):
        """Loads questions from the endless exam file."""
        file_path = DataManager.get_endless_exam_file_path(exam_tag)
        if not file_path.exists():
            return {}

        module_name = f"data.{exam_tag}.{exam_tag}_endless"
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            print(f"Error: Could not create module spec for {file_path}")
            return {}
        
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            if hasattr(module, 'PRACTICE_DATA'):
                return module.PRACTICE_DATA
            else:
                print(f"Warning: {file_path} does not contain PRACTICE_DATA.")
                return {}
        except Exception as e:
            print(f"Error loading endless exam data from {file_path}: {e}")
            return {}

    @staticmethod
    def append_questions_to_endless_file(exam_tag, new_questions_data):
        """Appends new questions to the endless exam file."""
        file_path = DataManager.get_endless_exam_file_path(exam_tag)
        
        # Load current data, merge, and rewrite the entire file for robustness
        current_data = DataManager.load_endless_exam_data(exam_tag)
        
        # Merge new sections into existing data
        current_data.update(new_questions_data) 
        
        with open(file_path, "w") as f:
            f.write(f"# {exam_tag}_endless.py - AI Generated Questions\n\n")
            f.write(f"EXAM_TAG = \"{exam_tag}\"\n\n")
            f.write(f"EXAM_TITLE = \"{exam_tag.upper()}: Endless AI Exam\"\n\n")
            f.write(f"PRACTICE_DATA = {json.dumps(current_data, indent=4)}\n")

    @staticmethod
    def overwrite_endless_file(exam_tag, new_data):
        """Completely overwrites the endless file with distilled data."""
        file_path = DataManager.get_endless_exam_file_path(exam_tag)
        with open(file_path, "w") as f:
            f.write(f"# {exam_tag}_endless.py - Distilled & Refined Questions\n\n")
            f.write(f"EXAM_TAG = \"{exam_tag}\"\n\n")
            f.write(f"EXAM_TITLE = \"{exam_tag.upper()}: Endless AI Exam (Distilled)\"\n\n")
            f.write(f"PRACTICE_DATA = {json.dumps(new_data, indent=4)}\n")
        print(f"Successfully distilled and updated {file_path}")

    _question_generator_instance = None

    @classmethod
    def get_question_generator(cls):
        if cls._question_generator_instance is None:
            cls._question_generator_instance = QuestionGenerator(
                api_key=OPENAI_API_KEY,
                api_base=OPENAI_API_BASE,
                model=OPENAI_MODEL
            )
        return cls._question_generator_instance

    @staticmethod
    async def generate_and_append_questions(exam_tag, existing_questions_context=None, num_questions=NUM_QUESTIONS_TO_GENERATE):
        """Generates new questions and appends them to the endless exam file."""
        generator = DataManager.get_question_generator()
        generated_raw_questions = await generator.generate_questions( # This is an async call
            exam_tag, existing_questions_context, num_questions
        )
        if generated_raw_questions:
            # Create a new section for these generated questions
            section_name = f"AI Generated Section {int(time.time())}" # Unique section name
            formatted_data = {section_name: generated_raw_questions}
            DataManager.append_questions_to_endless_file(exam_tag, formatted_data)
            print(f"Appended {len(generated_raw_questions)} new questions to {exam_tag}_endless.py")
        else:
            print(f"No questions generated for {exam_tag}.")