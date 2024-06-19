"""
Move all zeros to the end of the list while maintaining the order of non-zero numbers.

The program takes a predefined list of numbers and creates a new list
where all zeros are moved to the end, preserving the order of non-zero numbers.

Example:
    Input: [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]
"""

numbers = [0, 31, 0, 3, 12, 0, 1]

# Create a new list with non-zero numbers and new list with zero numbers
non_zero_numbers = [num for num in numbers if num != 0]
zero_numbers = [num for num in numbers if num == 0]

# Concatenate the two lists to get the final result
result = non_zero_numbers + zero_numbers

print(f'Result: {result}')
