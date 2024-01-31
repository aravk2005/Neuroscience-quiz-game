def ask_question(question, options, answer_key, count):
    print(question)
    for option in options:
        print(option)
    answer = input("What is your answer? Please give a letter: ")
    if answer == answer_key:
        count += 1
        print(f"Correct! {count}/{len(questions)}")
    else:
        print("Incorrect!")
    return count
    
questions = [
    ("1. What part of the brain is responsible for regulating fear?",
     ["a. Hippocampus", "b. Amygdala", "c. Thalamus", "d. Cereberum"], "b"),
    ("2. Tim got arrested for a DUI last week, which part of his brain was affected at the time of his arrest?",
     ["a. Medula", "b. Basil ganglia", "c. Pons", "d. Cerebellum"], "d"),
    ("3. What mental disorder can result from a lack of norepinepherin?",
     ["a. Bipolar disorder", "b. Depression", "c. Schizophrenia", "d. BPD"], "b"),
    ("4. Which one of the following is NOT an example of a hallucinogen?",
     ["a. Marijuana", "b. Magic Mushrooms", "c. LSD", "d. Salvia"], "a"),
    ("5. Which neurotransmitter is released when an individual exercises?",
     ["a. Dopamine", "b. Seratonin", "c. Endorphins", "d. Acetylcholine"], "c"),
    ("6. What is the name(s) of the neuron that connects the afferent and efferent neurons?",
     ["a. Connecting neuron", "b. Interneuron", "c. Joining Neuron", "d. All of the above"], "c"),
    ("7. Which part of the brain is the substantia nigra in?",
     ["a. Midbrain", "b. Hindbrain", "c. Forebrain", "d. Temporal lobe"], "a"),
    ("8. What is the function of the substantia nigra?",
     ["a. To allow the transport of sodium ions", "b. The creation of cerebrospinal fluid",
      "c. The regulation of brain blood flow", "d. Dopamine production"], "d"),
    ("9. Resting potential in a neuron is negative?",
     ["a. True", "b. False"], "a"),
    ("10. Which of the following is NOT a type of Glial cell: ",
     ["a. Astroglia", "b. Oligondendroglia", "c. Parenchyma", "d. Ependymal"], "c")
]

name = input("Enter your name: ")
print(f"Hello {name}, welcome to the PS101 Neuroscience quiz!")
print("Good luck >:)")

count = 0
for question, options, answer_key in questions:
    count = ask_question(question, options, answer_key, count)

print(f"Your score: {count}/{len(questions)}")
if count < len(questions) / 2:
    print("Practice some more and try again!")
else:
    print("Great job! Good luck on your test :)")
