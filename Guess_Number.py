import random

rnd = random.randint(1, 100)

while True:
    try:
        guessed_number = int(input("Guess the number:"))
        print(guessed_number)

    except ValueError:
        print("It's not a number!")
        continue

    if guessed_number < rnd:
        print("Too small!")
        continue
    elif guessed_number > rnd:
        print("Too big!")
        continue
    elif guessed_number == rnd:
        print("You win!")
    break
