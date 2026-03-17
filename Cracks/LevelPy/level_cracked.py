import tkinter as tk
from tkinter import messagebox

def check():
    # This string will be embedded in the binary data section
    if entry.get() == "Saad_79_Percent":
        messagebox.showinfo("Win", "Flag: {CYTH0N_TR4NSL4T10N_2026}")
    else:
        messagebox.showerror("Fail", "Try again!")

root = tk.Tk()
root.title("Binary Vault")
tk.Label(root, text="System Password", font=("Helvetica", 20), fg="blue").pack()
entry = tk.Entry(root, show="*")
entry.pack()
tk.Button(root, text="Unlock", command=check).pack()
root.mainloop()
