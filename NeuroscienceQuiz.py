

name = input("Enter your name: ")
print(f"Hello {name}, welcome to the PS101 Neuroscience quiz!")
print("Goodluck >:)")
print("--------------")
count = 0

print("1. What part of the brain is responsible for regulating fear?")
parts = ["a. Hippocampus", "b. Amygdala", "c. Thalamus", "d. Cereberum"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "b":
    count += 1
    print(f"Correct! {count}/1")
else:
    print("Incorrect!")

print("2. Tim got arrested for a DUI last week, which part of his brain was affected at the time of his arrest?")
parts = ["a. Medula", "b. Basil ganglia", "c. Pons", "d. Cerebellum"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter ")
if answer == "d":
    count += 1
    print(f"Correct! {count}/2 ")
else:
    print("incorrect!")

print("3. What mental disorder can result from a lack of norepinepherin?")
parts = ["a. Bipolar disorder", "b. Depression", "c. Schizophrenia", "d. BPD"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "b":
    count += 1
    print(f"Correct! {count}/3")
else:
    print("Incorrect!")

print("4. Which one of the following is NOT an example of a hallucinogen? ")
parts = ["a. Marijuana", "b. Magic Mushrooms", "c. LSD", "d. Salvia"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "a":
    count += 1
    print(f"Correct! {count}/4")
else:
    print("Incorrect!")

print("5. Which neurotransmitter is released when an individual exercises? ")
parts = ["a. Dopamine", "b. Seratonin", "c. Endorphins", "d. Acetylcholine"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "c":
    count += 1
    print(f"Correct! {count}/5")
else:
    print("Incorrect!")

print("6. What is the name(s) of the neuron that connects the afferent and efferent neurons?")
parts = ["a. Connecting neuron", "b. Interneuron", "c. Joining Neuron", "d. All of the above"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "c":
    count += 1
    print(f"Correct! {count}/6")
else:
    print("Incorrect!")

print("7. Which part of the brain is the substantia nigra in?")
parts = ["a. Midbrain", "b. Hindbrain", "c. Forebrain", "d. Temporal lobe"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "a":
    count += 1
    print(f"Correct! {count}/7")
else:
    print("Incorrect!")

print("8. What is the function of the substantia nigra?")
parts = ["a. To allow the transport of sodium ions", "b. The creation of cerebrospinal fluid", "c. The regulation of brain blood flow", "d. Dopamine production"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "d":
    count += 1
    print(f"Correct! {count}/8")
else:
    print("Incorrect!")

print("9. Resting potential in a neuron is negative ?")
parts = ["a. True", "b. False"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "a":
    count += 1
    print(f"Correct! {count}/9")
else:
    print("Incorrect!")

print("10. Which of the following is NOT a type of Glial cell: ")
parts = ["a. Astroglia", "b. Oligondendroglia", "c. Parenchyma", "d. Ependymal"]
for part in parts:
    print(part)
answer = input("What is your answer? Please give a letter: ")
if answer == "c":
    count += 1
    print(f"Correct! {count}/10")
else:
    print("Incorrect!")

score = print(f"Your score: {count}/10")
if count < 6: 
    print("Practice some more and try again!")
else:
    print("Great job! goodluck on your test :)")
