"""
Multiply the digits of a user-entered integer until the result is less than or equal to 9.
"""

number = int(input("Enter an integer: "))

# Start a loop that continues as long as 'number' is greater than 9
while number > 9:
    digit_product = 1

    while number != 0:
        # Multiply 'digit_product' by the last digit of 'number' using the modulo operator
        digit_product *= number % 10
        number //= 10  # Update 'number' by dividing it by 10 using integer division to remove the last digit

    number = digit_product

print(f"Result: {number}")
