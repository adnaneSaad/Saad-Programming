import tkinter as tk
from tkinter import ttk, messagebox
import random

class OrientationApp:
    def __init__(self, master):
        self.master = master
        master.title("Smart Orientation Assistant")
        master.geometry("550x700")
        
        # Initialize Tkinter Variables for inputs
        self.best_subject_var = tk.StringVar(value="None")
        self.math_var = tk.BooleanVar()
        self.science_exp_var = tk.BooleanVar()
        self.writing_var = tk.BooleanVar()
        self.reading_var = tk.BooleanVar()
        self.languages_var = tk.BooleanVar()
        self.communication_var = tk.BooleanVar()
        self.tech_var = tk.BooleanVar()
        self.creativity_var = tk.BooleanVar()
        self.precision_var = tk.BooleanVar()
        
        # Configure Grid
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)

        self.create_widgets()
        
    def create_widgets(self):
        
        # Title
        title_label = ttk.Label(self.master, text="Smart Orientation Assistant", 
                                font=('Arial', 18, 'bold'), foreground='blue')
        title_label.grid(row=0, column=0, columnspan=2, pady=(15, 5), sticky="n")
        
        ttk.Label(self.master, text="Answer the questions below to find your path.", 
                  font=('Arial', 10)).grid(row=1, column=0, columnspan=2, pady=(0, 15), sticky="n")

        # --- 1. Best Subject (Dropdown) ---
        ttk.Label(self.master, text="1. Best School Subject:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        subjects = ["None", "Math", "Science", "Arabic", "English", "French"]
        subject_combo = ttk.Combobox(self.master, textvariable=self.best_subject_var, 
                                     values=subjects, state="readonly")
        subject_combo.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # --- Questions 2 - 10 (Checkboxes) ---
        q_row = 3
        
        # List of questions and their corresponding BooleanVars
        questions = [
            ("2. Do you enjoy mathematics?", self.math_var),
            ("3. Do you like scientific experiments?", self.science_exp_var),
            ("4. Do you enjoy writing and expressing your ideas?", self.writing_var),
            ("5. Do you enjoy reading books?", self.reading_var),
            ("6. Do you love learning new languages?", self.languages_var),
            ("7. Are you good at communicating with others?", self.communication_var),
            ("8. Do you enjoy computers, programming, and devices?", self.tech_var),
            ("9. Do you consider yourself creative and enjoy inventing solutions?", self.creativity_var),
            ("10. Are you precise in your work and care about details?", self.precision_var)
        ]
        
        for text, var in questions:
            cb = ttk.Checkbutton(self.master, text=text, variable=var)
            cb.grid(row=q_row, column=0, columnspan=2, padx=10, pady=2, sticky="w")
            q_row += 1

        # --- Submit Button ---
        submit_button = ttk.Button(self.master, text="Calculate My Path", command=self.calculate_path)
        submit_button.grid(row=q_row, column=0, columnspan=2, pady=20)
        q_row += 1
        
        # --- Results Display Section ---
        self.result_frame = ttk.LabelFrame(self.master, text="📊 Evaluation Results")
        self.result_frame.grid(row=q_row, column=0, columnspan=2, padx=10, pady=10, sticky="ew")
        self.result_frame.columnconfigure(0, weight=1)
        self.result_frame.columnconfigure(1, weight=1)

        self.path_labels = {}
        paths = ["Scientific Path", "Literature Path", "Languages Path", "Technical Path"]
        
        for i, path in enumerate(paths):
            ttk.Label(self.result_frame, text=f"{path}:").grid(row=i, column=0, padx=5, pady=2, sticky="w")
            # Store references to the percentage labels for updating later
            self.path_labels[path] = ttk.Label(self.result_frame, text="0%")
            self.path_labels[path].grid(row=i, column=1, padx=5, pady=2, sticky="e")
            
        self.best_path_label = ttk.Label(self.master, text="Click 'Calculate My Path' to see your suggestion.", 
                                        font=('Arial', 12, 'bold'), wraplength=500)
        self.best_path_label.grid(row=q_row + 1, column=0, columnspan=2, pady=15)
        
    def calculate_path(self):
        # Reset Scores
        science = 0
        literature = 0
        languages = 0
        tech = 0

        # --- 1 - Best School Subject ---
        best = self.best_subject_var.get()
        if best == "Math":
            science += 3
            tech += 2
        elif best == "Science":
            science += 3
        elif best == "Arabic":
            literature += 3
        elif best in ["English", "French"]:
            languages += 3

        # --- 2 - 10 Yes/No Questions (using BooleanVar.get()) ---
        if self.math_var.get():
            science += 2
            tech += 1
        
        if self.science_exp_var.get():
            science += 2

        if self.writing_var.get():
            literature += 2

        if self.reading_var.get():
            literature += 2

        if self.languages_var.get():
            languages += 2

        if self.communication_var.get():
            languages += 1
            literature += 1

        if self.tech_var.get():
            tech += 3

        if self.creativity_var.get():
            tech += 2
            literature += 1

        if self.precision_var.get():
            science += 1
            tech += 1

        # Total points and Percentage calculation
        total = science + literature + languages + tech
        
        if total == 0:
            messagebox.showinfo("No Input", "Please select your best subject or answer some questions.")
            return

        ps = round((science / total) * 100)
        pl = round((literature / total) * 100)
        pla = round((languages / total) * 100)
        pt = round((tech / total) * 100)
        
        # --- Update Results Display ---
        self.path_labels["Scientific Path"].config(text=f"{ps}%")
        self.path_labels["Literature Path"].config(text=f"{pl}%")
        self.path_labels["Languages Path"].config(text=f"{pla}%")
        self.path_labels["Technical Path"].config(text=f"{pt}%")

        # Determine the Best Path
        highest = max(ps, pl, pla, pt)
        
        result_text = "\n👉 The best suggested path for you is:\n"
        
        if highest == ps:
            result_text += "🎯 **Scientific Path**\n✔ You enjoy logic, precision, and scientific experiments."
        elif highest == pl:
            result_text += "🎯 **Literature Path**\n✔ You are strong in writing, reading, and expression."
        elif highest == pla:
            result_text += "🎯 **Languages Path**\n✔ You love learning languages and communicating with people."
        elif highest == pt:
            result_text += "🎯 **Technical Path**\n✔ You enjoy computers, creativity, and technological work."
        else:
            result_text = "No clear dominant path. Try answering more questions."
            
        self.best_path_label.config(text=result_text)

# --- Main Program Execution ---
if __name__ == '__main__':
    root = tk.Tk()
    app = OrientationApp(root)
    root.mainloop()
