"""
This application runs in the console.
The result of its operation is the answer to whether the user guessed the number drawn by the computer.
"""


import random

rnd = random.randint(1, 100)

while True:
    try:
        guessed_number = int(input("Guess the number:"))
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
