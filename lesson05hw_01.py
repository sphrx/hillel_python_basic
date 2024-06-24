"""
Program to check if the entered string can be a variable name in Python.

A variable cannot:
* start with a digit
* contain uppercase letters
* contain spaces or punctuation characters (except underscore "_")
* be any of the reserved keywords
Additionally, the complete variable name should consist of no more than one underscore "_".

As a result of the check, either True is printed if such a variable name is allowed, or False if not.
"""

# Input a string from the user
variable_name = input("Enter a variable name: ")

# Check if the variable name is valid
validation = True

# Check if the variable name starts with a digit
if variable_name[0].isdigit():
    validation = False

# Check if the variable name contains uppercase letters, spaces,
# or punctuation (except underscore)
for char in variable_name:
    if (char.isupper() or char.isspace() or
            (char in "!\"#$%&'()*+,-./:;<=>?@[\\]^`{|}~" and char != '_')):
        validation = False
        break

# Check if the variable name contains more than one underscore
if variable_name.count('_') > 1:
    validation = False

# Check if the variable name is a reserved keyword
reserved_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try',
    'while', 'with', 'yield'
]
if variable_name in reserved_keywords:
    validation = False

# Print the result
print(validation)
