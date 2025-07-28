# Python Beginner Exercise: Number Fun!
# -----------------------------------------

# Goal:
# Learn how to use variables, expressions, statements, and some built-in functions
# such as print(), input(), and type().

# Instructions:
# Step 1: Ask the user to enter their favorite number using the input() function.
#         Remember: input() returns a string, so you must convert it to an int using int().
# Step 2: Store the result in a variable called 'number'.
# Step 3: Do the following calculations and store each in a new variable:
#         a) Add 10 to the number → store in 'plus_ten'
#         b) Multiply the number by 3 → store in 'times_three'
#         c) Square the number (use **) → store in 'squared'
#         d) Divide the number by 2 using floor division (//) → store in 'half_floor'
#         e) Find the remainder when divided by 5 → store in 'mod_five'
# Step 4: Print all results using print(), and also print the type using type()

# Example Output:
# Enter your favorite number: 7
# Number + 10 = 17 <class 'int'>
# Number * 3 = 21 <class 'int'>
# Number squared = 49 <class 'int'>
# Number // 2 = 3 <class 'int'>
# Number % 5 = 2 <class 'int'>

# Bonus (optional):
# Try changing your number to a float (e.g., 7.5) and use float(input()) instead of int(input()).
# See how the types change!

number = float(input("Enter your favorite number: "))
print("You entered:", number)

plus_ten = number + 10
print("Number + 10 = ", plus_ten, type(plus_ten))

times_three = number * 3
print('Number * 3 = ', times_three,type(times_three))

squared = number ** 2
print("Number squared = ", squared,type(squared))

half_floor = number // 2
print('Number // 2 = ', half_floor, type(half_floor))

mod_five = number % 5
print('Number % 5 = ' , mod_five , type(mod_five))