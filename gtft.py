import random

FLAVORTEXTS = [
    ("Its peach-shaped shell serves as storage for a potent poison. It makes poisonous mochi and serves them to people and Pokémon.", "Pecharunt"),
    ("This seems to be the Iron Serpent mentioned in an old book. The Iron Serpent is said to have turned the land to ash with its lightning.", "Miraidon"),
    ("Once it accepts you as a friend, it tries to show its affection with a hug. Letting it do that is dangerous—it could easily shatter your bones.", "Bewear"),
    ("It has a vicious temperament. Beware if it raises its tail straight up. This is a signal that it is about to pounce and bite.", "Persian"),
    ("To protect themselves from danger, they hide their true identities by transforming into people and Pokémon.", "Zorua"),
    ("BLANK is a ruffian with a short temper. It can pulverize anything by swinging around the chain on its neck.", "Okidogi"),
    ("BLANK beats its glossy wings to scatter pheromones that captivate people and Pokémon.", "Fezandipiti"),
    ("BLANK keeps itself somewhere safe while it toys with its foes, using psychokinesis to induce intense dizziness.", "Munkidori")

]

def main(x):
    correctCount = 0
    random.shuffle(FLAVORTEXTS)
    for text, correctAnswer in FLAVORTEXTS:
        answer = input(f"{text} ")
        if answer.capitalize() == correctAnswer:
            print("Correct!")
            correctCount += 1
        elif answer.capitalize() == "Stop":
            print(f"Hmmm. Back already. Looks like you got {correctCount} prompts correct. Not to shabby. Want to try again?")
            print("(press 'y' to start again or 'n' to exit)")
            while True:
                i = input()
                if i == "y":
                    x = input("Great! How many prompts would you like: ")
                    main(x)
                elif i == "n":
                    print("No worries! I'll be here if you want to try again!")
                    exit()
        else:
            print(f"Incorrect. The answer is {correctAnswer}.")
    print(f"Wow! Incredible job trainer! You made it through the whole module! And you got {correctCount} correct answers. Well done! Come back and try again when we have more new prompts.")
    exit()

print("Hello Pokemon trainers! Today we will be testing your knowledge of Pokemon lore and behaviors.")
print("(press 'y' to continue)")
while True:
    i = input()
    if i == "y":
        break

print("The following prompts have all been taken from the most recently discovered Pokemon. So I hope you've been following the news! HAHAHA!")
print("(press 'y' to continue)")
while True:
    i = input()
    if i == "y":
        break

print("Now then. If you need to exit the program, simply enter 'STOP' at any point and you'll return here to me. Are you ready trainer?!")
print("(press 'y' to continue)")
while True:
    i = input()
    if i == "y":
        x = input("Great! How many prompts would you like: ")
        main(x)
    elif i == "n":
        exit()