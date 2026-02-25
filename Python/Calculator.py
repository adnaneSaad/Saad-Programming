#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from tkinter import messagebox, ttk

Page = tk.Tk()
Page.title("Saad's Calculator")
Page.geometry("400x300")
L1 = tk.Label(Page, text = "Welcome To Saad's Calculator!", fg = "blue", font = ("Arial", 16, "bold"))
L1.pack(padx = 10, pady = 10)

T1 = ttk.Label(Page, text = "Enter the first operator")
T1.pack()

TE1 = ttk.Entry(Page)
TE1.pack()

O = ttk.Label(Page, text = "Enter an Operator")
O.pack()

OE = ttk.Entry(Page)
OE.pack()

T2 = ttk.Label(Page, text = "Enter the second operator")
T2.pack()

TE2 = ttk.Entry(Page)
TE2.pack()

def CalcSubmit():
    try:
        t1 = float(TE1.get())
        o = OE.get()
        t2 = float(TE2.get())

        if o == "+":
            Final = t1 + t2
        elif o == "-":
            Final = t1 - t2
        elif o == "*":
            Final = t1 * t2
        elif o == "/":
            Final = t1 / t2
    except ValueError:
        messagebox.showerror("Input Error",
                             f"Please fill the first and second labels with numbers.\n\nDon't forget to fill the operator label with either '+, -, * or /' ",
                             parent = Page)
        return

    messagebox.showinfo("Results",
                        f"{t1} {o} {t2} = {Final}",
                        parent = Page)

CalcB = tk.Button(Page, text = "Calculate!", bg = "grey", fg = "black", command = CalcSubmit)
CalcB.pack(padx = 10, pady = 10)

Page.mainloop()
