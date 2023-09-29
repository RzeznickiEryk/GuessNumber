print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach.")
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
