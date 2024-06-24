'''
A simple calculator program that performs mathematical operations (+, -, *, /).
The user is prompted to enter two numbers and an operator.
The program checks if the operator is valid and if there is no division by zero.
The program continues to ask the user if they want to continue until the user enters "n".
'''

while True:
    # Input the first number
    number_one = float(input("Enter the first number: "))

    # Input an operator
    operator = input("Enter operator(+, -, *, /): ")

    # Input the second number
    number_two = float(input("Enter the second number: "))

    # Check if the operator is valid and execute the operation
    if operator == '+':
        result = number_one + number_two
    elif operator == '-':
        result = number_one - number_two
    elif operator == '*':
        result = number_one * number_two
    elif operator == '/':
        result = number_one / number_two if number_two != 0 else "Error: division by zero!"
    else:
        result = "Error: invalid operator!"

    print(f"Result: {result}")

    # Ask the user if they want to continue
    continue_calculation = input("Do you want to continue? (y/n): ")
    if continue_calculation.lower() != 'y':
        break

print("Calculator is stopped.")