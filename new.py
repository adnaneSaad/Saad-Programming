print("==================================================")
print("Hello, Welcome to the Smart Orientation Assistant!")
print("==================================================")

science = 0
languages = 0
tech = 0
latest = ""

#1 - the best school subject
print("What's the best subject for you: Maths, science, English, Arabic or ICT?")
Q1 = input("==>")
if Q1 == "Maths":
    science += 4
elif Q1 == "science":
    science += 2
elif Q1 == "English":
    languages += 4
elif Q1 == "Arabic":
    languages += 4
elif Q1 == "ICT":
    tech += 4

#2 - love math
print("Do you enjoy Mathematics?")
Q2 = input("==>")
if Q2 == "yes":
    science += 2
    tech += 1

#3 - love Scientific experiments
print("Do you like scientific experiments?")
Q3 = input("==>")
if Q3 == "yes":
    science += 2

last = max(tech, languages, science)
if last == tech:
    latest = "tech"
elif last == languages:
    latest = "languages"
elif last == science:
    latest = "science"

print("The best option is:", latest)
