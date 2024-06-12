"""
A simple calculator program that performs mathematical operations (+, -, *, /).
The user is prompted to enter two numbers and an operator.
The program checks if the operator is correct and if there is no division by zero.
"""

# Input the first number
number_one = float(input("Enter the first number: "))

# Input an operator
operator = input("Enter operator(+, -, *, /): ")

# Input the second number
number_two = float(input("Enter the second number: "))

# Check if the operator is correct and execute the operation
if operator == '+':
    result = number_one + number_two
    print(f"Result: {number_one} + {number_two} = {result}")
elif operator == '-':
    result = number_one - number_two
    print(f"Result: {number_one} - {number_two} = {result}")
elif operator == '*':
    result = number_one * number_two
    print(f"Result: {number_one} * {number_two} = {result}")
elif operator == '/':
    if number_two != 0: # Check for division by zero
        result = number_one / number_two
        print(f"Result: {number_one} / {number_two} = {result}")
    else:
        print("Error: division by zero!")
else:
    print("Error: invalid operator!")

# """
# A simple calculator program.
#
# This program takes a mathematical expression as input in the format
# "operand1operator operand2" (e.g., "3+4"), performs the specified
# operation, and prints the result.
#
# Supported operations: addition (+), subtraction (-), multiplication (*),
# division (/).
# """
#
# # Input expression
# expression = input("Enter an expression (e.g., 3+4): ")
#
# # Find the operator
# operator = (
#     "+" if "+" in expression
#     else "-" if "-" in expression
#     else "*" if "*" in expression
#     else "/" if "/" in expression
#     else ""
# )
#
# if operator != "":
#     # Split into operands
#     parts = expression.split(operator)
#     left_operand = float(parts[0])
#     right_operand = float(parts[1])
#
#     # Perform the operation
#     result = (
#         left_operand + right_operand if operator == "+"
#         else left_operand - right_operand if operator == "-"
#         else left_operand * right_operand if operator == "*"
#         else left_operand / right_operand if right_operand != 0
#         else "Error: division by zero!"
#     )
#     print("Error: invalid input format!" if result == ""
#         else "Result: " + str(result)
#     )
# else:
#     print("Error: invalid input format!")

