# Python Exercise: Computer Guesses the User's Number
# Estimated Time: 20–25 minutes

# Description:
# Write a Python program where the **computer** tries to guess a number that the **user** is thinking of.
# The number is between 0 and 100 (inclusive), and the user keeps it secret.

# The computer makes random guesses within a range, and after each guess, the user gives a hint using one of the following:
# - 'h' → if the guess is too **high**
# - 'l' → if the guess is too **low**
# - 'c' → if the guess is **correct**

# The computer starts with a guessing range from 0 to 100 and updates this range after each guess based on the user's feedback.

# The guessing continues until the user confirms that the computer's guess is correct.

# Requirements:
# - Use a `while` loop to repeat guessing until the correct number is found.
# - Use `random.randint(lower_bound, upper_bound)` to make each guess.
# - Use two variables (`lower_bound`, `upper_bound`) to keep track of the current guessing range.
# - Use a counter variable (`guess_count`) to track the number of guesses.
# - Accept only 'h', 'l', or 'c' as valid user inputs; otherwise, print an error message and repeat the input.

# Example:
# (User is thinking of 42)
# → My 1 guss is: 67 (h = high | l = low | c = correct)?
# → User types: h
# → My 2 guss is: 15 (h = high | l = low | c = correct)?
# → User types: l
# → My 3 guss is: 41 (h = high | l = low | c = correct)?
# → User types: l
# → My 4 guss is: 44 (h = high | l = low | c = correct)?
# → User types: h
# → My 5 guss is: 42 (h = high | l = low | c = correct)?
# → User types: c
# → Output: "My 5 guss is 42, and it's correct :)!"

# Extra:
# - After each game, ask the user if they want to play again (enter 'y' or 'n').
# - Keep the code clean and readable by using descriptive variable names.

import random

comp_guess = 0

print("Pick a number between 0 and 100. I'll guess that number. Ready? (y for continue)")
ready = input()

while ready == 'y':
    lower_bound = 0
    upper_bound = 100
    user_tip = ''
    guess_count = 1
    while user_tip != 'c':
        comp_guess = random.randint(lower_bound, upper_bound)
        print('My', guess_count, 'guss is: ', comp_guess, ' (h = high | l = low | c = correct)?')
        user_tip = input()
        if user_tip == 'h':
            upper_bound = comp_guess - 1
            guess_count += 1
        elif user_tip == 'l':
            lower_bound = comp_guess + 1
            guess_count += 1
        elif user_tip == 'c':
            print('My', guess_count, 'guss is ', comp_guess, "and it's correct :)!")
            print('Wow, I am the smartest computer in the world!  :D')
        else:
            print('Invalid input! pleas enter only h for high, l for low and c for correct answers!')
    print('Do you want to continue? (y or n)')
    ready = input()