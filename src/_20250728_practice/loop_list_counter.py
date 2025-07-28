# Python Exercise: List Building and Loop Control
# Estimated time: 20 minutes
# from itertools import count

# Task:
# Write a program that asks the user to enter numbers one by one and adds them to a list (suggested list name: numbers).
# The user should type "done" to finish entering numbers.
# Use a while loop (while True) to collect inputs.
# Use break to exit the loop when the user types "done".
# Use continue to skip any input that is not a valid number (use try-except block).

# After the list is created, use a for loop with range (for i in range(...)) and a counter variable
# (suggested counter name: count) to print each number in the list along with its index (starting from 1).

# Example:
# Input: 5, 10, abc, 3, done
# Output:
# 1: 5.0
# 2: 10.0
# 3: 3.0

# Bonus:
# After the loop, calculate and print the sum of all numbers in the list (suggested variable name: total_sum).

numbers = []
while True:
    num = input('Please enter a number (or done to finish): ')
    if num == 'done':
        break

    try:
        num = float(num)
        numbers.append(num)
    except ValueError:
        print('It is not a correct number. Please try again!')
        continue

for count in range(len(numbers)):
    print(f"{count + 1}: {numbers[count]}")

total_sum = 0
for num in numbers:
    total_sum += num

print('\nTotal sum: ', total_sum)