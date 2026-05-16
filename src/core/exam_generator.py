import random
import importlib
import tkinter as tk

# The PracticeExamApp is now in src.gui.app, but not directly used in this module.

def load_all_questions(data_modules):
    """Dynamically loads and combines questions from all 4 data files."""
    all_questions = []
   
    for module_name in data_modules:
        try:
            # Use importlib to get the actual sub-module
            module = importlib.import_module(module_name)
            print(f"Loaded module: {module_name}")
            
            # Extract the questions from each section
            if hasattr(module, 'PRACTICE_DATA'):
                for section_questions in module.PRACTICE_DATA.values():
                    all_questions.extend(section_questions)
                print(f"✅ Loaded {len(all_questions)} total questions so far.")
            else:
                print(f"⚠️ Warning: {module_name} has no PRACTICE_DATA attribute.")
                
        except ImportError as e:
            print(f"⚠️ Warning: Could not find {module_name}. Error: {e}")
            
    return all_questions

def generate_master_exam(data_modules):
    # 1. Pool all questions together
    question_pool = load_all_questions(data_modules)
    
    if not question_pool:
        print("❌ Error: No questions loaded. Please check your file names.")
        return None
        
    print(f"\nTotal questions in pool: {len(question_pool)}")
    
    # 2. Randomly select exactly 70 questions (or the max available if under 70)
    target_q_count = min(70, len(question_pool))
    selected_questions = random.sample(question_pool, target_q_count)
    
    # 3. Re-package them into the format the GUI expects (10 sections of 7)
    master_practice_data = {}
    questions_per_section = 7
    
    # Calculate how many sections we need
    num_sections = (target_q_count + questions_per_section - 1) // questions_per_section
    
    for i in range(num_sections):
        start_idx = i * questions_per_section
        end_idx = start_idx + questions_per_section
        
        # Name the sections generically for the simulated exam
        section_name = f"Exam Block {i + 1} (Mixed Topics)"
        master_practice_data[section_name] = selected_questions[start_idx:end_idx]
        
    return master_practice_data
