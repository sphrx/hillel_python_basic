"""
Create a new list with the first, third, and second-to-last elements from a user-inputted list.

The program prompts the user to enter a list of numbers separated by spaces.
It then creates a new list containing three elements from the original list:
- The first element
- The third element
- The second-to-last element

Example:
    Input: 1 2 3 4 5 6 7 8 9
    Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    New list: [1, 3, 8]
"""

# Prompt the user to enter a list of numbers
input_string = input("Enter a list of numbers separated by spaces: ")

# Split the input string into a list of strings and convert each element to an integer
numbers = [int(num) for num in input_string.split()]

# Check if the list contains at least 3 elements
if len(numbers) < 3:
    print("Error: The list must contain at least 3 elements.")
else:
    # Create a new list with the first, third, and second-to-last elements
    new_list = [numbers[0], numbers[2], numbers[-2]]

    print(f"Original list: {numbers}")
    print(f"New list: {new_list}")
