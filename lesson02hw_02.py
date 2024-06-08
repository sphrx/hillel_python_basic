
"""
A program to turn a 5-digit number backwards.

The user enters a 5-digit positive integer.
The program divides this number into separate digits using the // and % operations.
Then it forms a new number from the digits in reverse order.
"""

# The user enters a 5-digit number.
number = int(input("Enter a 5-digit number: "))

# We get the sequence of digits of a number using arithmetic operators.
digit_one = number // 10000
digit_two = (number % 10000) // 1000
digit_three = (number % 1000) // 100
digit_four = (number % 100) // 10
digit_five = number % 10

# Generate a new number in reverse order using f-string
reversed_number = int(f"{digit_five}{digit_four}{digit_three}{digit_two}{digit_one}")

# Print the result
print(f"Turn the number over: {reversed_number}")
