import tkinter as tk
import tkmacosx as tkx
from tkinter import messagebox
from tkinter import Tk
import json
import asyncio
import threading
import random
from config.config import GENERATION_DELAY_SECONDS, NUM_QUESTIONS_TO_GENERATE
import os

class PracticeExamApp:
    root: Tk
    exam_tag: str
    exam_title: str
    practice_data: object
    is_endless_mode: bool
    is_master_mode: bool
    endless_file_path: str
    question_generation_thread: threading.Thread = None
    generation_run_counter: int = 0
    launcher_root: Tk

    def __init__(self, root, exam_tag, exam_title, practice_data, is_endless_mode=False, is_master_mode=False, endless_file_path=None, launcher_root=None):
        self.root = root
        self.root.title(exam_title)
        self.root.geometry("800x680")
        self.root.configure(bg="#f4f6f8")

        # Data Management
        self.exam_tag = exam_tag
        self.is_endless_mode = is_endless_mode
        self.is_master_mode = is_master_mode
        self.endless_file_path = endless_file_path
        self.launcher_root = launcher_root
        self.practice_data = practice_data
        self._randomize_options()
        self.sections = list(self.practice_data.keys())
        
        # Shuffle section order for Master or Endless modes
        if self.is_master_mode or self.is_endless_mode:
            random.shuffle(self.sections)
        
        # Session State
        self.current_section_idx = 0
        self.current_q_idx = 0
        self.score = 0
        self.section_score = 0
        self.all_results = {}

        # Styles
        self.font_title = ("Helvetica", 16, "bold")
        self.font_q = ("Helvetica", 14)
        self.font_opt = ("Helvetica", 14)
        self.font_small = ("Helvetica", 12)
        self.bg_color = "#f4f6f8"

        self.setup_ui()

        if self.is_endless_mode:
            self.question_generation_thread = threading.Thread(target=self._start_question_generation_loop, daemon=True)
            self.question_generation_thread.start()
            self.load_question()
        else:
            # Save/Resume Logic for non-endless modes
            if os.path.exists(exam_tag + "_progress.json"):
                if messagebox.askyesno("Resume Session", "A saved session was found. Would you like to resume where you left off?"):
                    self.load_progress()
                else:
                    self.load_question()
            else:
                self.load_question()

        # Bind the close event to stop the generation thread
        self.root.protocol("WM_DELETE_WINDOW", self._on_closing)

    def setup_ui(self):
        # Header
        self.lbl_section = tk.Label(self.root, text="", font=self.font_title, bg=self.bg_color, fg="#005a9e")
        self.lbl_section.pack(pady=15)

        self.lbl_progress = tk.Label(self.root, text="", font=self.font_opt, bg=self.bg_color)
        self.lbl_progress.pack()

        # Question Frame
        self.frame_q = tk.Frame(self.root, bg="white", bd=2, relief="groove", padx=20, pady=20)
        self.frame_q.pack(fill="x", padx=30, pady=15)

        self.lbl_question = tk.Label(self.frame_q, text="", font=self.font_q, bg="white", wraplength=650, justify="left")
        self.lbl_question.pack(anchor="w", pady=(0, 15))

        self.var_choice = tk.IntVar()
        self.var_choice.set(-1)
        self.radios = []
        for i in range(4):
            rb = tk.Radiobutton(self.frame_q, text="", variable=self.var_choice, value=i, font=self.font_opt, bg="white", wraplength=600, justify="left")
            rb.pack(anchor="w", pady=5)
            self.radios.append(rb)

        # Controls Frame
        self.frame_controls = tk.Frame(self.root, bg=self.bg_color)
        self.frame_controls.pack(pady=10)

        self.btn_submit = tkx.Button(self.frame_controls, text="Submit", font=self.font_opt, bg="#ADEFD1", fg="black", command=self.submit_answer)
        self.btn_submit.grid(row=0, column=0, padx=10)

        self.btn_next = tkx.Button(self.frame_controls, text="Next", font=self.font_opt, bg="#006DAD", fg="white", state="disabled", command=self.next_question)
        self.btn_next.grid(row=0, column=1, padx=10)

        # Save Progress Button (only for non-endless mode)
        self.btn_save = tkx.Button(self.frame_controls, text="Save & Exit", font=self.font_opt, bg="#f39c12", fg="white", command=self.save_progress)
        self.btn_save.grid(row=0, column=2, padx=10)

        # Explanation
        self.lbl_explanation = tk.Label(self.root, text="", font=self.font_opt, bg=self.bg_color, wraplength=650, justify="left", fg="#333333")
        self.lbl_explanation.pack(pady=10)

        if self.is_endless_mode:
            self.btn_save.config(text="Exit Endless Exam", command=self._on_closing)

    def save_progress(self):
        state = {
            "c_sec": self.current_section_idx,
            "c_q": self.current_q_idx,
            "score": self.score,
            "sec_score": self.section_score,
            "results": self.all_results,
            "active_sections": self.sections
        }
        with open(self.exam_tag + "_progress.json", "w") as f:
            json.dump(state, f)
        messagebox.showinfo("Saved", "Progress saved successfully! Exiting.")
        self.root.destroy()

    def load_progress(self):
        try:
            with open(self.exam_tag + "_progress.json", "r") as f:
                state = json.load(f)
            self.current_section_idx = state["c_sec"]
            self.current_q_idx = state["c_q"]
            self.score = state["score"]
            self.section_score = state["sec_score"]
            self.all_results = state["results"]
            self.sections = state["active_sections"]
            self.load_question()
        except Exception:
            messagebox.showerror("Error", "Failed to load save file.")
            # If loading fails, start fresh
            self.current_section_idx = 0
            self.current_q_idx = 0
            self.score = 0
            self.section_score = 0
            self.all_results = {}
            self.load_question()

    def load_question(self):
        if self.current_section_idx >= len(self.sections):
            return self._handle_empty_section()
            
        section_name = self.sections[self.current_section_idx]
        questions = self.practice_data.get(section_name, [])
        
        if not questions or self.current_q_idx >= len(questions):
            return self._handle_empty_section()
            
        q_data = questions[self.current_q_idx]
        self.lbl_section.config(text=section_name)
        self.lbl_progress.config(text=f"Question {self.current_q_idx + 1} of {len(self.practice_data[section_name])}")
        self.lbl_question.config(text=q_data["q"])
        self.lbl_explanation.config(text="")
        
        self.var_choice.set(-1)
        self.btn_submit.config(state="normal")
        self.btn_next.config(state="disabled")

        for i, option in enumerate(q_data["options"]):
            self.radios[i].config(text=option, fg="black", state="normal")

    def submit_answer(self):
        if self.var_choice.get() == -1: return
        
        section_name = self.sections[self.current_section_idx]
        q_data = self.practice_data[section_name][self.current_q_idx]
        correct_idx = q_data["answer"]
        selected_idx = self.var_choice.get()

        for rb in self.radios: rb.config(state="disabled")
        self.btn_submit.config(state="disabled")
        self.btn_next.config(state="normal")

        if selected_idx == correct_idx:
            self.radios[selected_idx].config(fg="green")
            self.score += 1
            self.section_score += 1
            res = "✅ Correct! "
        else:
            self.radios[selected_idx].config(fg="red")
            self.radios[correct_idx].config(fg="green")
            res = "❌ Incorrect. "

        self.lbl_explanation.config(text=res + q_data["explanation"])

    def next_question(self):
        if self.is_endless_mode:
            self.current_q_idx += 1
            section_name = self.sections[self.current_section_idx]
            if self.current_q_idx < len(self.practice_data[section_name]):
                self.load_question()
            else:
                # Reached end of current section in endless mode
                self.current_section_idx += 1
                self.current_q_idx = 0
                self._reload_endless_data(force_load=True)
        else:
            self.current_q_idx += 1
            section_name = self.sections[self.current_section_idx]

            if self.current_q_idx < len(self.practice_data[section_name]):
                self.load_question()
            else:
                self.finalize_section()

    def _handle_empty_section(self):
        """Handles cases where a section might be empty (e.g., after reloading endless data)."""
        messagebox.showinfo("No Questions", "No questions available in this section. Waiting for more to be generated.")
        # Disable controls until new questions are loaded
        self.btn_submit.config(state="disabled")
        self.btn_next.config(state="disabled")
        self.lbl_question.config(text="Waiting for AI to generate more questions...")
        self.lbl_explanation.config(text="")
        for rb in self.radios:
            rb.config(text="", state="disabled")

    def _randomize_options(self):
        """Randomizes the order of questions within sections and options for each question."""
        if not self.practice_data:
            return
        for section_name in self.practice_data:
            # Shuffle the order of questions within the section
            random.shuffle(self.practice_data[section_name])
            for q in self.practice_data[section_name]:
                # Store the text of the correct answer, shuffle, and update index
                correct_text = q["options"][q["answer"]]
                random.shuffle(q["options"])
                q["answer"] = q["options"].index(correct_text)

    def _reload_endless_data(self, force_load=False):
        from src.core.data_loader import DataManager # Import here to avoid circular dependency
        new_data = DataManager.load_endless_exam_data(self.exam_tag)
        
        if not new_data:
            # If we are strictly out of bounds of our current memory, show the waiting screen
            if self.current_section_idx >= len(self.sections):
                self._handle_empty_section()
            return

        # Detect transition from initial random pool (blocks of 7) to AI file
        is_from_random_pool = self.sections and self.sections[0].startswith("Random Block")
        
        self.practice_data = new_data
        self._randomize_options()
        self.sections = list(self.practice_data.keys())
        
        # Shuffle blocks for endless mode
        random.shuffle(self.sections)
        
        if is_from_random_pool:
            # Reset to start of the AI file when transitioning from the initial pool
            self.current_section_idx = 0
            self.current_q_idx = 0
            self.load_question()
        elif self.current_section_idx < len(self.sections):
            # Only trigger UI update if we are moving to a new section (forced)
            # or if we were previously stuck on the waiting screen.
            if force_load or self.lbl_question.cget("text") == "Waiting for AI to generate more questions...":
                self.load_question()
        else:
            # Still no more sections available in the file
            self._handle_empty_section()

    def finalize_section(self):
        sec_name = self.sections[self.current_section_idx]
        self.all_results[sec_name] = {"correct": self.section_score, "total": len(self.practice_data[sec_name])}
        
        messagebox.showinfo("Section Complete", f"Score: {self.section_score}/{len(self.practice_data[sec_name])}")
        
        self.current_section_idx += 1
        self.current_q_idx = 0
        self.section_score = 0

        if self.current_section_idx < len(self.sections):
            self.load_question()
        else:
            if os.path.exists(self.exam_tag + "_progress.json"): os.remove(self.exam_tag + "_progress.json")
            self.show_final_score_card()

    def show_final_score_card(self):
        card = tk.Toplevel(self.root)
        card.title("Final Performance Report")
        card.geometry("600x700")
        card.configure(bg="white")

        tk.Label(card, text="FINAL SCORE CARD", font=self.font_title, bg="white", fg="#005a9e").pack(pady=20)

        all_perfect = True
        weak_sections = []
        
        res_frame = tk.Frame(card, bg="white")
        res_frame.pack(fill="both", expand=True, padx=40)

        for sec, stats in self.all_results.items():
            perc = (stats['correct'] / stats['total']) * 100
            if perc < 100: all_perfect = False
            if perc < 80: weak_sections.append(sec)
            
            icon = "✅" if perc >= 85 else "⚠️" if perc >= 70 else "❌"
            tk.Label(res_frame, text=f"{icon} {sec[:35]}... : {perc:.1f}%", font=self.font_small, bg="white", anchor="w").pack(fill="x")

        if all_perfect:
            msg, color = "🏆 PERFECT! You are ready for the exam!", "green"
        elif not weak_sections:
            msg, color = "🌟 GREAT JOB! You passed everything.", "#005a9e"
        else:
            msg, color = "📚 STUDY RECOMMENDATION: Retake the sections below.", "#d9534f"

        tk.Label(card, text=msg, font=("Helvetica", 12, "bold"), bg="white", fg=color, wraplength=500).pack(pady=15)

        if weak_sections:
            tkx.Button(card, text="Retake Weakest Sections", bg="#e67e22", fg="white", 
                       command=lambda: self.retake_logic(card, weak_sections)).pack(pady=10)

        tkx.Button(card, text="Exit App", command=self.root.quit, bg="#333", fg="white").pack(pady=10)

    def retake_logic(self, card_window, weak_list):
        card_window.destroy()
        self.sections = weak_list
        self.current_section_idx = 0
        self.current_q_idx = 0
        self.score = 0
        self.section_score = 0
        self.all_results = {}
        self.load_question()

    def _start_question_generation_loop(self):
        """Runs in a separate thread to continuously generate questions."""
        asyncio.run(self._async_question_generation_loop())

    async def _async_question_generation_loop(self):
        from src.core.data_loader import DataManager # Import here to avoid circular dependency
        self.generation_run_counter = 0
        while True:
            # Check if the exam window is still open
            if not self.root.winfo_exists():
                print("Exam window closed, stopping question generation thread.")
                break

            # Get some context from current questions to avoid duplicates
            current_questions_context = []
            for section in self.practice_data.values():
                current_questions_context.extend(section)
            
            # Only pass a few questions as context to save tokens
            recent_questions_for_context = random.sample(current_questions_context, min(5, len(current_questions_context)))

            self.generation_run_counter += 1
            print(f"Endless Exam: Starting generation run {self.generation_run_counter} for {self.exam_tag}...")
            await DataManager.generate_and_append_questions(
                self.exam_tag,
                existing_questions_context=recent_questions_for_context,
                num_questions=NUM_QUESTIONS_TO_GENERATE
            )
            
            # After generating, if the current section is empty, try to reload
            # This handles the initial empty state or if user finished all questions
            try:
                if self.current_section_idx >= len(self.sections) or self.lbl_question.cget("text") == "Waiting for AI to generate more questions...":
                    self.root.after(100, self._reload_endless_data)
            except Exception:
                pass

            await asyncio.sleep(GENERATION_DELAY_SECONDS) # Pause between runs

    def _on_closing(self):
        """Handles the window closing event for endless mode."""
        if self.question_generation_thread and self.question_generation_thread.is_alive():
            print("Stopping question generation thread (daemon will exit with main process).")
        self.root.destroy()
        #if self.launcher_root:
        #    self.launcher_root.destroy() # Also destroy the hidden launcher root
