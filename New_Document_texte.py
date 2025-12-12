print("Welcome to the smart orientation assistant!!")

scientific = 0
languistic = 0
tech = 0
last = ""

print("What's the best subject for you: Math, Science, English, Arabic or ICT?")
Q1 = input("==>")
if Q1 == "Science":
    scientific = scientific + 4
    tech = tech + 1
elif Q1 == "Math":
    scientific = scientific + 4
    tech = 3
elif Q1 == "English":
    languistic = languistic + 4
elif Q1 == "Arabic":
    languistic = languistic + 4
elif Q1 == "ICT":
    tech = tech + 4

print("Do you like experiments??")
Q2 = input("==>")
if Q2 == "Yes":
    scientific = scientific + 3
elif Q2 == "No":
    scientific = scientific

print("Do you enjoy Mathematics?")
Q3 = input("==>")
if Q3 == "Yes":
    scientific = scientific + 3
    tech = tech + 2
elif Q3 == "No":
    scientific = scientific
    tech = tech

print("Do you like writing stories, books, or reading them?")
Q4 = input("==>")
if Q4 == "Yes":
    languistic = languistic + 3   
elif Q4 == "No":
    languistic = languistic

print("Do you like devices, computers or programming?")
Q5 = input("==>")
if Q5 == "Yes":
    tech = tech + 4
elif Q5 == "No":
    tech = tech


print(f"Scientific = "{scientific})
print(f"Languistic = "{languistic})
print(f"tech = "{tech})
