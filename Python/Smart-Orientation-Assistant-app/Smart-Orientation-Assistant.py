#!/usr/bin/env python
# coding: utf-8

import tkinter as tk
from tkinter import messagebox, ttk

class UniversalOrientationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Universal Orientation Assistant - Moroccan Baccalaureate")
        self.root.geometry("600x800")
        self.root.configure(bg="#f5f6fa")

        self.db = {
            "Physical Sciences (PC)": {
                "nat": {"Mathematics": 7, "Physics/Chem": 7, "SVT": 5, "English": 2, "Philosophy": 2},
                "reg": {"French": 4, "Arabic": 2, "Islamic Ed": 2, "Hist-Geo": 2}
            },
            "Life Sciences (SVT)": {
                "nat": {"Mathematics": 7, "Physics/Chem": 5, "SVT": 7, "English": 2, "Philosophy": 2},
                "reg": {"French": 4, "Arabic": 2, "Islamic Ed": 2, "Hist-Geo": 2}
            },
            "Mathematical Sciences - A": {
                "nat": {"Mathematics": 9, "Physics/Chem": 7, "SVT": 3, "English": 2, "Philosophy": 2},
                "reg": {"French": 4, "Arabic": 2, "Islamic Ed": 2, "Hist-Geo": 2}
            }
        }

        self.entries = {}
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Baccalaureate GPA & Orientation System", 
                 font=("Arial", 16, "bold"), bg="#f5f6fa", fg="#2f3640").pack(pady=10)

        frame_top = tk.Frame(self.root, bg="#f5f6fa")
        frame_top.pack(pady=5)
        tk.Label(frame_top, text="Select Target Stream:", font=("Arial", 10), bg="#f5f6fa").pack(side="left")
        
        self.stream_var = tk.StringVar()
        self.combo = ttk.Combobox(frame_top, textvariable=self.stream_var, values=list(self.db.keys()), 
                                  state="readonly", width=35)
        self.combo.pack(side="left", padx=10)
        self.combo.bind("<<ComboboxSelected>>", self.update_fields)

        self.fields_container = tk.LabelFrame(self.root, text="Enter Marks (0-20)", 
                                              font=("Arial", 11, "bold"), padx=20, pady=20, bg="white")
        self.fields_container.pack(fill="both", expand=True, padx=20, pady=10)

    def update_fields(self, event=None):
        for widget in self.fields_container.winfo_children():
            widget.destroy()
        self.entries = {}

        stream = self.stream_var.get()
        data = self.db[stream]

        tk.Label(self.fields_container, text="--- National Exam Subjects (50%) ---", 
                 fg="#2980b9", bg="white", font=("Arial", 9, "bold")).pack()
        for sub in data['nat'].keys():
            self.create_entry(sub, "nat")

        tk.Label(self.fields_container, text="--- Regional Exam Subjects (25%) ---", 
                 fg="#27ae60", bg="white", font=("Arial", 9, "bold")).pack(pady=(10, 0))
        for sub in data['reg'].keys():
            self.create_entry(sub, "reg")

        tk.Label(self.fields_container, text="--- School Assessment (25%) ---", 
                 fg="#e67e22", bg="white", font=("Arial", 9, "bold")).pack(pady=(10, 0))
        self.create_entry("Yearly Average", "muraqaba")

        tk.Button(self.fields_container, text="Calculate & Recommend", command=self.calculate, 
                  bg="#44bd32", fg="white", font=("Arial", 11, "bold"), cursor="hand2").pack(pady=20)

    def create_entry(self, label, category):
        row = tk.Frame(self.fields_container, bg="white")
        row.pack(fill="x", pady=2)
        tk.Label(row, text=label, width=22, anchor="w", bg="white").pack(side="left")
        entry = tk.Entry(row, justify="center")
        entry.pack(side="right", expand=True, fill="x", padx=5)
        entry.insert(0, "10.0")
        self.entries[f"{category}_{label}"] = entry

    def recommend_stream(self):
        # Safely fetch marks, defaulting to 0 if the subject isn't in the current view
        try:
            m = float(self.entries.get("nat_Mathematics").get()) if self.entries.get("nat_Mathematics") else 0
            s = float(self.entries.get("nat_SVT").get()) if self.entries.get("nat_SVT") else 0
            p = float(self.entries.get("nat_Physics/Chem").get()) if self.entries.get("nat_Physics/Chem") else 0
            
            if m >= s and m >= p: return "Mathematical Sciences"
            if s > m and s >= p: return "Life Sciences (SVT)"
            return "Physical Sciences (PC)"
        except:
            return "Unknown"

    def calculate(self):
        try:
            stream = self.stream_var.get()
            if not stream:
                messagebox.showwarning("Warning", "Please select a stream first!")
                return

            data = self.db[stream]
            
            nat_score, nat_coeff_sum = 0, 0
            for sub, coeff in data['nat'].items():
                mark = float(self.entries[f"nat_{sub}"].get())
                nat_score += mark * coeff
                nat_coeff_sum += coeff
            nat_avg = nat_score / nat_coeff_sum

            reg_score, reg_coeff_sum = 0, 0
            for sub, coeff in data['reg'].items():
                mark = float(self.entries[f"reg_{sub}"].get())
                reg_score += mark * coeff
                reg_coeff_sum += coeff
            reg_avg = reg_score / reg_coeff_sum

            muraqaba = float(self.entries["muraqaba_Yearly Average"].get())
            final_gpa = (nat_avg * 0.5) + (reg_avg * 0.25) + (muraqaba * 0.25)

            # Get the recommendation based on marks
            suggestion = self.recommend_stream()

            messagebox.showinfo("Analysis Result", 
                                f"Current Stream: {stream}\n"
                                f"Estimated GPA: {final_gpa:.2f} / 20\n\n"
                                f"💡 Recommendation: Based on your marks, you might excel most in: {suggestion}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers (0-20) in all fields.")

if __name__ == "__main__":
    root = tk.Tk()
    app = UniversalOrientationApp(root)
    root.mainloop()
