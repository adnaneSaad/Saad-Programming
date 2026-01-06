from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Smart Orientation Assistant")
root.geometry("450x750")      # width x height
<<<<<<< HEAD
root.resizable(True, True)  # lock resizing
=======
root.resizable(False, False)  # lock resizing

#====================================================================================================================================================================#
Title = Label(root, text="Hello, this is Smart Orientation Assistant!!", fg="blue")
Title.grid(row=0, column=0)

# Scores
science = literature = languages = tech = 0
ps = pl = pla = pt = 0   # initialize percentages

# 1 - Best School Subject 
L1 = Label(root, text="What is the subject you are best at: Math, Science, Arabic, English or French?")
L1.grid(row=1, column=0)

Q1 = ttk.Combobox(root, values = ["Math", "Science", "Arabic", "English", "French"], state = "readonly")
Q1.set("Select")
Q1.grid(row=2, column=0)

# 2 - Love for Mathematics
L2 = Label(root, text="Do you enjoy Mathematics?")
L2.grid(row=3, column=0)

Q2 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q2.grid(row=4, column=0)
Q2.set("Select")

# 3 - Love for scientific experiments
L3 = Label(root, text="Do you like scientific experiments?")
L3.grid(row=5, column=0)

Q3 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q3.set("Select")
Q3.grid(row=6, column=0)

# 4 - Writing
L4 = Label(root, text="Do you enjoy writing and expressing your ideas?")
L4.grid(row=7, column=0)

Q4 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q4.set("Select")
Q4.grid(row=8, column=0)

# 5 - Reading books
L5 = Label(root, text="Do you enjoy reading books?")
L5.grid(row=9, column=0)

Q5 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q5.set("Select")
Q5.grid(row=10, column=0)

# 6 - Languages
L6 = Label(root, text="Do you enjoy learning new languages?")
L6.grid(row=11, column=0)

Q6 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q6.set("Select")
Q6.grid(row=12, column=0)

# 7 - Communication
L7 = Label(root, text="Are you good at communicating with others?")
L7.grid(row = 13, column=0)

Q7 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q7.set("Select")
Q7.grid(row = 14, column = 0)

# 8 - Computers & Technology
L8 = Label(root, text="Do you enjoy computers, programming, and devices?")
L8.grid(row=15, column=0)

Q8 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q8.set("Select")
Q8.grid(row=16, column=0)

# 9 - Creativity
L9 = Label(root, text="Do you consider yourself creative and enjoy inventing solutions?")
L9.grid(row=17, column=0)

Q9 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q9.set("Select")
Q9.grid(row=18, column=0)

# 10 - Precision and details
L10 = Label(root, text="Are you precise in your work and care about details?")
L10.grid(row=19, column=0)

Q10 = ttk.Combobox(root, values = ["Yes", "No"], state = "readonly")
Q10.set("Select")
Q10.grid(row = 20, column=0)

# Results labels#9:08##9:17#9:22#
F1 = Label(root, text="📊 Evaluation Results")
F1.grid(row=22, column=0)

F2 = Label(root, text=f"Scientific Path : {ps}%")
F2.grid(row=23, column=0)

F3 = Label(root, text=f"Literature Path : {pl}%")
F3.grid(row=24, column=0)

F4 = Label(root, text=f"Languages Path : {pla}%")
F4.grid(row=25, column=0)

F5 = Label(root, text=f"Technical Path : {pt}%")
F5.grid(row=26, column=0)

F6 = Label(root, text="👉 The best suggested path for you is:")
F6.grid(row=27, column=0)

F7 = Label(root, text="")  # placeholder for best path
F7.grid(row=28, column=0)

F8 = Label(root, text="")  # placeholder for description
F8.grid(row=29, column=0)

# Main function
def Submit():
    global science, literature, languages, tech, ps, pl, pla, pt
    science = literature = languages = tech = 0

    # 1 - Best School Subject 
    if Q1.get() == "Math":
        science += 3
        tech += 2
    elif Q1.get() == "Science":
        science += 3
    elif Q1.get() == "Arabic":
        literature += 3
    elif Q1.get() == "English":
        languages += 3
    elif Q1.get() == "French":
        languages += 3

    # 2 - Love for Mathematics
    if Q2.get() == "Yes":
        science += 2
        tech += 1

    # 3 - Love for scientific experiments
    if Q3.get() == "Yes":
        science += 2

    # 4 - Writing
    if Q4.get() == "Yes":
        literature += 2

    # 5 - Reading books
    if Q5.get() == "Yes":
        literature += 2

    # 6 - Languages
    if Q6.get() == "Yes":
        languages += 2

    # 7 - Communication
    if Q7.get() == "Yes":
        languages += 1
        literature += 1

    # 8 - Computers & Technology
    if Q8.get() == "Yes":
        tech += 3

    # 9 - Creativity
    if Q9.get() == "Yes":
        tech += 2
        literature += 1

    # 10 - Precision and details
    if Q10.get() == "Yes":
        science += 1
        tech += 1

    # Total points
    total = science + literature + languages + tech
    if total > 0:
        ps = round((science / total) * 100)
        pl = round((literature / total) * 100)
        pla = round((languages / total) * 100)
        pt = round((tech / total) * 100)
    else:
        ps = pl = pla = pt = 0

    # Refreshing Labels "percentage"
    F2.config(text=f"Scientific Path : {ps}%")
    F3.config(text=f"Literature Path : {pl}%")
    F4.config(text=f"Languages Path : {pla}%")
    F5.config(text=f"Technical Path : {pt}%")

    # Suggested path
    highest = max(ps, pl, pla, pt)
    if highest == ps:
        F7.config(text="🎯 Scientific Path")
        F8.config(text="✔ You enjoy logic, precision, and scientific experiments.")
    elif highest == pl:
        F7.config(text="🎯 Literature Path")
        F8.config(text="✔ You are strong in writing, reading, and expression.")
    elif highest == pla:
        F7.config(text="🎯 Languages Path")
        F8.config(text="✔ You love learning languages and communicating with people.")
    else:
        F7.config(text="🎯 Technical Path")
        F8.config(text="✔ You enjoy computers, creativity, and technological work.")

# Final - Submit button
submit = Button(root, text="Submit", bg = "black", fg = "white", font = ("Cascadia Mono", 30, "bold"), command = Submit, padx=15, pady=5)
submit.grid(row=21, column=0)

#====================================================================================================================================================================#
root.mainloop()

