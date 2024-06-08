"""
A program to display the digits of a 4-digit number in a column with an empty line between them.

The user enters a 4-digit number from the keyboard.
The program divides this number into separate digits using the // and % operations.
Each digit is displayed separately on a new line.
"""

# User enters a 4-digit number
number = int(input("Enter a 4-digit number: "))

# We get the sequence of digits of a number using arithmetic operators.
digit_one = number // 1000
digit_two = (number % 1000) // 100
digit_three = (number % 100) // 10
digit_four = number % 10

# Print the digits one by one in a column
print(digit_one)
print(digit_two)
print(digit_three)
print(digit_four)

"""
A program to display the digits of a 4-digit number in a column with an empty line between them.

The user enters a 4-digit number from the keyboard.
The program divides this number into separate digits using the // and % operations.
Each digit is displayed separately with an indent (empty line) between the digits.
"""

# number = int(input("Enter a 4-digit number: ")) # User enters a 4-digit number
#
# # We get the sequence of digits of a number using arithmetic operators.
# digit_one = number // 1000
# digit_two = (number % 1000) // 100
# digit_three = (number % 100) // 10
# digit_four = number % 10
#
# # Print the digits one by one in a column with an empty line between them
# print(digit_one)
# print()
# print(digit_two)
# print()
# print(digit_three)
# print()
# print(digit_four)
