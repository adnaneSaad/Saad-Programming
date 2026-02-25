#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from tkinter import messagebox, ttk
root = tk.Tk()
root.title("Username Length Check")
root.geometry("250x150")
L = tk.Label(root, text = "Enter Your Username!", fg = "blue", font = ("Arial", 16, "bold"))
L.pack(padx = 10, pady = 10)

E = ttk.Entry(root)
E.pack()

def submit():
    UN = str(E.get())

    if len(UN) >= 5:
        Var = "Username Accepted"
    else:
        Var = "Username Denied 'too short'"

    messagebox.showinfo(
        "User Name Status",
        Var,
        parent = root
        )

B = tk.Button(root, text = "Click To Submit!", fg = "black", bg = "grey", command = submit)
B.pack(padx = 10, pady = 10)
root.mainloop()
