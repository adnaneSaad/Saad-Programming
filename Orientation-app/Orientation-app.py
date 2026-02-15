#!/usr/bin/env python3
# coding: utf-8
import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk()
root.title("Saad's Orientation Assistant")
#==========================================================================================================================================#
MainLabel1 = tk.Label(root, text = "Welcome to Saad's Orientation app for 2AC!", font=("Arial", 16, "bold") ,foreground="Blue")
MainLabel1.pack()

MainLabel2 = tk.Label(root, text = "Write down your marks to see which orientation is best for you", font=("Arial", 12), pady = 10)
MainLabel2.pack()
#==========================================================================================================================================#
Frame = ttk.Frame(root)
Frame.pack(pady = 20)
#==========================================================================================================================================#
Label1 = ttk.Label(Frame, text = "Physics:", font = ("Arial", 10))
Label1.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 10)

Entry1 = ttk.Entry(Frame)
Entry1.grid(row = 1, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
Label2 = ttk.Label(Frame, text = "Hist.Geo:", font = ("Arial", 10))
Label2.grid(row = 2, column = 0, sticky = "w", padx = 10, pady = 10)

Entry2 = ttk.Entry(Frame)
Entry2.grid(row = 2, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
Label3 = ttk.Label(Frame, text = "ICT:", font = ("Arial", 10))
Label3.grid(row = 3, column = 0, sticky = "w", padx = 10, pady = 10)

Entry3 = ttk.Entry(Frame)
Entry3.grid(row = 3, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
Label4 = ttk.Label(Frame, text = "Edu.Islamique", font = ("Arial", 10))
Label4.grid(row = 4, column = 0, sticky = "w", padx = 10, pady = 10)

Entry4 = ttk.Entry(Frame)
Entry4.grid(row = 4, column = 1, sticky = "w", padx = 10, pady = 10)

#==========================================================================================================================================#
Label5 = ttk.Label(Frame, text = "English", font = ("Arial", 10))
Label5.grid(row = 5, column = 0, sticky = "w", padx = 10, pady = 10)

Entry5 = ttk.Entry(Frame)
Entry5.grid(row = 5, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
Label6 = ttk.Label(Frame, text = "Arabic", font = ("Arial", 10))
Label6.grid(row = 6, column = 0, sticky = "w", padx = 10, pady = 10)

Entry6 = ttk.Entry(Frame)
Entry6.grid(row = 6, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
Label7 = ttk.Label(Frame, text = "French", font = ("Arial", 10))
Label7.grid(row = 7, column = 0, sticky = "w", padx = 10, pady = 10)

Entry7 = ttk.Entry(Frame)
Entry7.grid(row = 7, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
Label8 = ttk.Label(Frame, text = "Maths", font = ("Arial", 10))
Label8.grid(row = 8, column = 0, sticky = "w", padx = 10, pady = 10)

Entry8 = ttk.Entry(Frame)
Entry8.grid(row = 8, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
Label9 = ttk.Label(Frame, text = "SVT", font = ("Arial", 10))
Label9.grid(row = 9, column = 0, sticky = "w", padx = 10, pady = 10)

Entry9 = ttk.Entry(Frame)
Entry9.grid(row = 9, column = 1, sticky = "w", padx = 10, pady = 10)
#==========================================================================================================================================#
def Submit():
    global Physics, HistGeo, ICT, EduIslamique, English, Arabic, French, Maths, SVT

    Physics           = float (Entry1.get())
    HistGeo           = float (Entry2.get())
    ICT               = float (Entry3.get())
    EduIslamique      = float (Entry4.get())
    English           = float (Entry5.get())
    Arabic            = float (Entry6.get())
    French            = float (Entry7.get())
    Maths             = float (Entry8.get())
    SVT               = float (Entry9.get())

    AuthenticEducation = (Physics * 0) + (HistGeo * 3) + (ICT * 2) + (EduIslamique * 4) + (English * 2) + (Arabic * 4) + (French * 3) + (Maths * 2) + (SVT * 2)

    ArtsAndHumanities  = (Physics * 0) + (HistGeo * 4) + (ICT * 2) + (EduIslamique * 0) + (English * 3) + (Arabic * 4) + (French * 4) + (Maths * 2) + (SVT * 2)

    ScientificTrunk    = (Physics * 4) + (HistGeo * 2) + (ICT * 2) + (EduIslamique * 0) + (English * 3) + (Arabic * 2) + (French * 3) +      (Maths * 4) + (SVT * 4)

    TechnologicalStump = (Physics * 4) + (HistGeo * 2) + (ICT * 3) + (EduIslamique * 0) + (English * 3) + (Arabic * 2) + (French * 3) + (Maths * 4) + (SVT * 0)

    Best = max(AuthenticEducation, ArtsAndHumanities, ScientificTrunk, TechnologicalStump)

    if (Best == AuthenticEducation):
        BestLabel = ttk.Label(Frame, text = "The Best Orientation For You is: 'Authentic Education'", font = ("Arial", 13))
        BestLabel.grid(row = 11, column = 0, padx = 15, pady = 15)

    elif(Best == ArtsAndHumanities):
        BestLabel = ttk.Label(Frame, text = "The Best Orientation For You is: 'Arts And Humanities'", font = ("Arial", 13))
        BestLabel.grid(row = 11, column = 0, padx = 15, pady = 15)

    elif(Best == ScientificTrunk):
        BestLabel = ttk.Label(Frame, text = "The Best Orientation For You is: 'Scientific Trunk'", font = ("Arial", 13))
        BestLabel.grid(row = 11, column = 0, padx = 15, pady = 15)

    elif(Best == TechnologicalStump):
        BestLabel = ttk.Label(Frame, text = "The Best Orientation For You is: 'Technological Stump'", font = ("Arial", 13))
        BestLabel.grid(row = 11, column = 0, padx = 15, pady = 15)
#==========================================================================================================================================#
SubmitButton = tk.Button(Frame, text = "Submit", bg = "gray", command = Submit)
SubmitButton.grid(row = 10, column = 0, columnspan = 2, pady = 10)
#==========================================================================================================================================#
root.mainloop()
