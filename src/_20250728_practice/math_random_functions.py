# Write a Python program that does the following:

# 1. Import the 'math' and 'random' libraries.
# 2. Define a function called `random_power_root(x)` that:
#    - Takes one number `x` as input.
#    - Generates a random integer between 2 and 5 using the random module.
#    - Calculates and returns the result of raising `x` to that power and then taking the square root of the result using the math module.
# 3. Define another function called `compare_to_threshold(value, threshold)` that:
#    - Returns True if value >= threshold, otherwise returns False.
# 4. In the main part of the code:
#    - Ask the user to input a number.
#    - Call the `random_power_root()` function with the user input.
#    - Print the returned result.
#    - Then call `compare_to_threshold()` with the result and a threshold of 100.
#    - Print whether the result is "Above or equal to threshold" or "Below threshold" based on the boolean output.

# Your program should demonstrate:
# - Importing standard libraries
# - Defining and calling functions with arguments and return values
# - Using random values and math functions
# - Using if/else with boolean logic

import math
import random


def random_power_root(x):
    random_number = random.randint(2, 5)
    print('Random number = ', random_number)
    return math.sqrt(x ** random_number)


def compare_to_threshold(value, threshold):
    if value >= threshold:
        return True
    else:
        return False


number = int(input('Please enter a number: '))
result = random_power_root(number)
print('Random power root: ', result)

if compare_to_threshold(result, 100):
    print('Above or equal to threshold')
else:
    print('Below threshold')