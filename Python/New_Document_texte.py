print("Welcome to the smart orientation assistant!!")

scientific = 0
languistic = 0
tech = 0
last = ""

print("What's the best subject for you: Math, Science, English, Arabic or ICT?")
Q1 = input("==>")
if Q1 == "science":
    scientific = scientific + 4
    tech = tech + 1
elif Q1 == "math":
    scientific = scientific + 4
    tech = 3
elif Q1 == "english":
    languistic = languistic + 4
elif Q1 == "arabic":
    languistic = languistic + 4
elif Q1 == "ict":
    tech = tech + 4

print("Do you like experiments??")
Q2 = input("==>")
if Q2 == "yes":
    scientific = scientific + 3
elif Q2 == "no":
    scientific = scientific

print("Do you enjoy Mathematics?")
Q3 = input("==>")
if Q3 == "yes":
    scientific = scientific + 3
    tech = tech + 2
elif Q3 == "no":
    scientific = scientific
    tech = tech

print("Do you like writing stories, books, or reading them?")
Q4 = input("==>")
if Q4 == "yes":
    languistic = languistic + 3   
elif Q4 == "no":
    languistic = languistic

print("Do you like devices, computers or programming?")
Q5 = input("==>")
if Q5 == "yes":
    tech = tech + 4
elif Q5 == "no":
    tech = tech


print(f"Scientific = {scientific}")
print(f"Languistic = {languistic}")
print(f"tech = {tech}")
