from dotenv import load_dotenv
load_dotenv()

import tkinter as tk
from tkinter import ttk, messagebox
import tkmacosx as tkx
from src.core.data_loader import DataManager
from src.gui.exam_ui import PracticeExamApp # Ensure this import is correct

class MainLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title("Endless Exam")
        self.root.geometry("500x420")
        self.root.configure(bg="#f0f2f5")

        # Load exam data
        self.all_exams = DataManager.discover_exams("data")
        if not self.all_exams:
            messagebox.showerror("Error", "No exam files found in /data directory.")
            self.root.destroy()
            return

        # Group exams by tag
        self.exam_series = {}
        for exam in self.all_exams:
            tag = exam['tag']
            if tag not in self.exam_series:
                self.exam_series[tag] = []
            self.exam_series[tag].append(exam)

        self.setup_ui()

    def setup_ui(self):
        style = ttk.Style()
        style.configure("TLabel", background="#f0f2f5", font=("Helvetica", 11))
        style.configure("TButton", font=("Helvetica", 10, "bold"))

        main_frame = tk.Frame(self.root, bg="#f0f2f5", padx=30, pady=30)
        main_frame.pack(expand=True, fill="both")

        tk.Label(main_frame, text="Exam Selection", font=("Helvetica", 16, "bold"), bg="#f0f2f5", fg="#005a9e").pack(pady=(0, 20))

        # 1. Select Series
        tk.Label(main_frame, text="Select Exam Series:", bg="#f0f2f5").pack(anchor="w")
        self.combo_series = ttk.Combobox(main_frame, values=sorted(list(self.exam_series.keys())), state="readonly")
        self.combo_series.pack(fill="x", pady=(5, 15))
        self.combo_series.bind("<<ComboboxSelected>>", self.on_series_selected)

        # 2. Select Mode
        tk.Label(main_frame, text="Select Mode:", bg="#f0f2f5").pack(anchor="w")
        self.mode_var = tk.StringVar(value="master")
        
        self.radio_master = tk.Radiobutton(main_frame, text="Master Simulator (70 Random Questions)", 
                                           variable=self.mode_var, value="master", bg="#f0f2f5", command=self.toggle_module_selection)
        self.radio_master.pack(anchor="w")
        
        self.radio_single = tk.Radiobutton(main_frame, text="Specific Module", 
                                           variable=self.mode_var, value="single", bg="#f0f2f5", command=self.toggle_module_selection)
        self.radio_single.pack(anchor="w")

        self.radio_endless = tk.Radiobutton(main_frame, text="Endless Exam (AI-Generated)",
                                            variable=self.mode_var, value="endless", bg="#f0f2f5", command=self.toggle_module_selection)
        self.radio_endless.pack(anchor="w")

        # 3. Specific Module Selection
        self.module_frame = tk.Frame(main_frame, bg="#f0f2f5")
        self.module_frame.pack(fill="x")
        self.lbl_module = tk.Label(self.module_frame, text="Select Specific Module:", bg="#f0f2f5")
        self.lbl_module.pack(anchor="w", pady=(10, 0))
        self.combo_modules = ttk.Combobox(self.module_frame, state="readonly", font=("Helvetica", 11))
        self.combo_modules.pack(fill="x", pady=(5, 15))

        # Start Button
        self.btn_start = tkx.Button(main_frame, text="START EXAM", bg="#006DAD", fg="white", 
                                   font=("Helvetica", 12, "bold"), command=self.launch_exam, height=2)
        self.btn_start.pack(fill="x", pady=(30, 0), ipady=20, side=tk.BOTTOM)

        # Initialize the visibility of the module selection based on the default mode
        self.toggle_module_selection()

    def on_series_selected(self, event):
        tag = self.combo_series.get()
        modules = [exam['title'] for exam in self.exam_series[tag]]
        self.combo_modules['values'] = modules
        if modules:
            self.combo_modules.current(0)
        # Ensure module selection is enabled/disabled correctly after series selection
        self.toggle_module_selection()

    def toggle_module_selection(self):
        is_single_mode = self.mode_var.get() == "single"
        has_series_selected = bool(self.combo_series.get())

        if is_single_mode and has_series_selected:
            self.combo_modules.config(state="readonly")
            self.lbl_module.config(fg="black")
        else:
            self.combo_modules.config(state="disabled")
            self.lbl_module.config(fg="gray")

    def launch_exam(self):
        tag = self.combo_series.get()
        if not tag:
            messagebox.showwarning("Warning", "Please select an exam series first.")
            return

        mode = self.mode_var.get()
        is_master_mode = False
        is_endless_mode = False
        endless_file_path = None
        
        if mode == "master":
            # Pool all modules for this tag
            series_list = self.exam_series[tag]
            exam_data = DataManager.get_randomized_exam(series_list, 70)
            title = f"{tag.upper()} Master Simulator (70 Qs)"
            is_master_mode = True
        elif mode == "endless":
            tag = self.combo_series.get()
            if not tag:
                messagebox.showwarning("Warning", "Please select an exam series first.")
                return

            endless_file_path = DataManager.get_endless_exam_file_path(tag)
            exam_data = DataManager.load_endless_exam_data(tag)
            title = f"{tag.upper()}: Endless AI Exam"
            is_endless_mode = True

            if not exam_data:
                # If endless file is empty, load 70 random questions from all modules for this tag
                messagebox.showinfo("Info", "Endless exam file is empty. Loading 70 random questions to start.")
                series_list = self.exam_series[tag]
                exam_data = DataManager.get_randomized_exam(series_list, 70)
                # Start generating questions in background
                # This will be handled by PracticeExamApp's init

            if not exam_data: # Still no data after trying random
                messagebox.showerror("Error", "No questions available to start the Endless Exam.")
                return

        elif mode == "single":
            # Find specific module
            module_title = self.combo_modules.get()
            selected_exam = next(e for e in self.exam_series[tag] if e['title'] == module_title)
            exam_data = selected_exam['data']
            title = selected_exam['title']

        else:
            messagebox.showerror("Error", "Invalid exam mode selected.")
            return

        if not exam_data:
            messagebox.showerror("Error", "No questions found in selection.")
            return

        # Hide the launcher window
        self.root.withdraw()
        # Launch PracticeExamApp
        exam_window = tk.Toplevel(self.root)

        # Ensure the entire application exits when the exam window is closed
        exam_window.protocol("WM_DELETE_WINDOW", self.root.destroy)
        # Handle programmatic destruction (like "Save & Exit") to close the hidden root
        exam_window.bind("<Destroy>", lambda e: self.root.destroy() if e.widget == exam_window else None)
        
        app = PracticeExamApp(exam_window, tag, title, exam_data, is_endless_mode=is_endless_mode, is_master_mode=is_master_mode, endless_file_path=endless_file_path, launcher_root=self.root)

if __name__ == "__main__":
    root = tk.Tk()
    launcher = MainLauncher(root)
    root.mainloop()