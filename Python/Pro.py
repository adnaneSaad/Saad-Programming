print("============================================")
print("Hello, this is Smart Orientation Assistant!!")
print("============================================")
def yes_no(question):
    answer = input(question + " (yes/no): ").strip().lower()
    return answer == "yes"

# Scores
science = 0
literature = 0
languages = 0
tech = 0

# 1 - Best School Subject
best = input("What is the subject you are best at? (Math/Science/Arabic/English/French): ").strip()

if best == "Math":
    science += 3
    tech += 2
elif best == "Science":
    science += 3
elif best == "Arabic":
    literature += 3
elif best in ["English", "French"]:
    languages += 3

# 2 - Love for Mathematics
if yes_no("Do you enjoy mathematics?"):
    science += 2
    tech += 1
# 3 - Love for scientific experiments
if yes_no("Do you like scientific experiments?"):
    science += 2

# 4 - Writing
if yes_no("Do you enjoy writing and expressing your ideas?"):
    literature += 2

# 5 - Reading books
if yes_no("Do you enjoy reading books?"):
    literature += 2

# 6 - Languages
if yes_no("Do you love learning new languages?"):
    languages += 2

# 7 - Communication
if yes_no("Are you good at communicating with others?"):
    languages += 1
    literature += 1

# 8 - Computers & Technology
if yes_no("Do you enjoy computers, programming, and devices?"):
    tech += 3

# 9 - Creativity
if yes_no("Do you consider yourself creative and enjoy inventing solutions?"):
    tech += 2
    literature += 1

# 10 - Precision and details
if yes_no("Are you precise in your work and care about details?"):
    science += 1
    tech += 1

# Total points
total = science + literature + languages + tech

# Percentage calculation
ps = round((science / total) * 100)
pl = round((literature / total) * 100)
pla = round((languages / total) * 100)
pt = round((tech / total) * 100)

print("\n=======================")
print("📊 Evaluation Results")
print("=======================\n")

print(f"Scientific Path : {ps}%")
print(f"Literature Path : {pl}%")
print(f"Languages Path : {pla}%")
print(f"Technical Path : {pt}%\n")

print("\n👉 The best suggested path for you is:\n")

highest = max(ps, pl, pla, pt)

if highest == ps:
    print("🎯 **Scientific Path**")
    print("✔ You enjoy logic, precision, and scientific experiments.\n")
elif highest == pl:
    print("🎯 **Literature Path**")
    print("✔ You are strong in writing, reading, and expression.\n")
elif highest == pla:
    print("🎯 **Languages Path**")
    print("✔ You love learning languages and communicating with people.\n")
else:
    print("🎯 **Technical Path**")
    print("✔ You enjoy computers, creativity, and technological work.\n")
