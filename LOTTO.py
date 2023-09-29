"""
This application runs in the console.
The result of its operation is information whether the user has drawn winning numbers in LOTTO.
"""

import random

rnd = sorted(random.sample(range(1, 50), 6))
entered_numbers = []
i = 1

while i < 7:

    try:
        your_number = int(input(f"Enter your {i} number:"))
        print(your_number)
    except ValueError:
        print("It's not a number!")
        continue

    if 1 <= your_number <= 49:
        if your_number in entered_numbers:
            print("You've already given this number. Name another one.")
            continue
        else:
            entered_numbers.append(your_number)
            i += 1
    else:
        print("Number outside the range 1 to 49. Enter another number.")
        continue


print(f"Your drawn numbers: {sorted(entered_numbers)}")
print(f"Lotto numbers: {rnd}")
matched_numbers = [number for number in entered_numbers if number in rnd]

if len(matched_numbers) >= 3:
    print(f"Congratulations! You matched {len(matched_numbers)} numbers")
else:
    print(f"Bardzo się starałeś lecz z gry wyleciałeś :(. Unfortunately, no win. You only matched {len(matched_numbers)} numbers.")
