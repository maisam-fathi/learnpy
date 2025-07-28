# Python Exercise: Age-Based Access Checker
# --------------------------------------------
# Goal: Practice using if, elif, else, Boolean variables, and logical/comparison operators.
# Estimated time: ~20 minutes

# Task:
# Write a program that:
# 1. Asks the user to enter their age using input().
# 2. Converts the input to an integer and stores it in a variable called `age`.
# 3. Based on the value of age, determine what kind of access the user has.

# Use the following rules:
# - If age is less than 0 or greater than 120 → Print "Invalid age" and stop.
# - If age is less than 13 → Print "You are a child. Access denied."
# - If age is between 13 and 17 (inclusive) → Print "Teen access granted. Limited content."
# - If age is between 18 and 64 → Print "Adult access granted. Full content."
# - If age is 65 or older → Print "Senior access granted. Enjoy our special section!"

# Bonus:
# - Create a Boolean variable `is_teenager` to store whether the user is between 13 and 17.
# - Use logical operators (and, or, not) at least once in your conditions.
# - Try comparing using ==, !=, <, >, <=, >=

# Example Output:
# Enter your age: 15
# Teen access granted. Limited content.
# Is teenager? True

# Make sure your program handles invalid input (e.g. "abc") without crashing. (Optional)

age = int(input('Enter your age: '))
is_teenager = False

if age < 0 or age > 120:
    print('Invalid age')
elif age < 13:
    print('You are a child. Access denied.')
elif 13 <= age <= 17:
    print('Teen access granted. Limited content.')
    is_teenager = True
elif 18 <= age <= 64:
    print('Adult access granted. Full content.')
elif age >= 65:
    print('Senior access granted. Enjoy our special section!')

if is_teenager:
    print('You are a teenager!')
else:
    print('You are not a teenager!')