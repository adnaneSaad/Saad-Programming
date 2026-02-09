#!/usr/bin/env python3
# coding: utf-8
import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.title("Saad's Orientation Assistant")
#===========================================================================================================================================#
MainLabel1 = tk.Label(root, text = "Welcome to Saad's Orientation app for 2AC!", font=("Arial", 16, "bold") ,foreground="Blue")
MainLabel1.pack()

MainLabel2 = tk.Label(root, text = "Write down your marks to see which orientation is best for you", font=("Arial", 12), pady=10)
MainLabel2.pack()
#===========================================================================================================================================#
Frame = ttk.Frame(root)
Frame.pack(pady = 20)
#===========================================================================================================================================#
Label1 = ttk.Label(Frame, text = "Physics:", font = ("Arial", 10))
Label1.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 10)

Entry1 = ttk.Entry(Frame)
Entry1.grid(row = 1, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#
Label2 = ttk.Label(Frame, text = "Hist.Geo:", font = ("Arial", 10))
Label2.grid(row = 2, column = 0, sticky = "w", padx = 10, pady = 10)

Entry2 = ttk.Entry(Frame)
Entry2.grid(row = 2, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#
Label3 = ttk.Label(Frame, text = "ICT:", font = ("Arial", 10))
Label3.grid(row = 3, column = 0, sticky = "w", padx = 10, pady = 10)

Entry3 = ttk.Entry(Frame)
Entry3.grid(row = 3, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#
Label4 = ttk.Label(Frame, text = "Edu.Islamique", font = ("Arial", 10))
Label4.grid(row = 4, column = 0, sticky = "w", padx = 10, pady = 10)

Entry4 = ttk.Entry(Frame)
Entry4.grid(row = 4, column = 1, sticky = "w", padx = 10, pady = 10)

#===========================================================================================================================================#
Label5 = ttk.Label(Frame, text = "English", font = ("Arial", 10))
Label5.grid(row = 5, column = 0, sticky = "w", padx = 10, pady = 10)

Entry5 = ttk.Entry(Frame)
Entry5.grid(row = 5, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#
Label6 = ttk.Label(Frame, text = "Arabic", font = ("Arial", 10))
Label6.grid(row = 6, column = 0, sticky = "w", padx = 10, pady = 10)

Entry6 = ttk.Entry(Frame)
Entry6.grid(row = 6, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#
Label7 = ttk.Label(Frame, text = "French", font = ("Arial", 10))
Label7.grid(row = 7, column = 0, sticky = "w", padx = 10, pady = 10)

Entry7 = ttk.Entry(Frame)
Entry7.grid(row = 7, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#
Label8 = ttk.Label(Frame, text = "Maths", font = ("Arial", 10))
Label8.grid(row = 8, column = 0, sticky = "w", padx = 10, pady = 10)

Entry8 = ttk.Entry(Frame)
Entry8.grid(row = 8, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#
Label9 = ttk.Label(Frame, text = "SVT", font = ("Arial", 10))
Label9.grid(row = 9, column = 0, sticky = "w", padx = 10, pady = 10)

Entry9 = ttk.Entry(Frame)
Entry9.grid(row = 9, column = 1, sticky = "w", padx = 10, pady = 10)
#===========================================================================================================================================#

#===========================================================================================================================================#
def Submit():
    global Physics, HistGeo, ICT, EduIslamique, English, Arabic, French, Maths, SVT

    Physics      = Entry1.get()
    HistGeo      = Entry2.get()
    ICT          = Entry3.get()
    EduIslamique = Entry4.get()
    English      = Entry5.get()
    Arabic       = Entry6.get()
    French       = Entry7.get()
    Maths        = Entry8.get()
    SVT          = Entry9.get()
#===========================================================================================================================================#
SubmitButton = tk.Button(Frame, text = "Submit", bg = "gray", command = Submit)
SubmitButton.grid(row = 10, column = 0, columnspan = 2, pady = 10)
#===========================================================================================================================================#
root.mainloop()
