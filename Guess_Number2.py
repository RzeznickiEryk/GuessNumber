"""
This application runs in the console. It works in such a way that the computer guesses the number that the user selects.
 The user uses the console to guide the computer to the correct result
 """


print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach. Używaj odpowiedzi 'You win', 'Too big', 'Too small'")
print("Naciśnij enter")
input()


minimum = 0
maximum = 1000

while True:

    guess = int((maximum - minimum) / 2) + minimum
    print(f'I guess: {guess}')
    answer = input("Is my answer correct?").lower()
    if answer == "you win":
        print("I win!")
        break
    elif answer == "too big":
        maximum = guess
        continue
    elif answer == "too small":
        minimum = guess
        continue
    else:
        print("Nie oszukuj")
        continue
