"""
Calculate the sum of elements with even indices and multiply it by the last element.

This program takes a list of integers and performs the following steps:
1. Check if the list is empty. If so, the result is 0.
2. If the list is not empty:
   - Calculate the sum of elements with even indices (0, 2, 4, ...).
   - Multiply the sum by the last element of the list.
3. Print the final result.

Example:
    Input: [0, 1, 2, 3, 4, 5]
    Output: Result: 30
"""

numbers = [3, 4, 5, 6, 2, 1]

# Check if the list is empty
if not numbers:
    result = 0
else:
    even_index_sum = 0  # Initialize the sum of even indexed numbers
    for i in range(0, len(numbers), 2):  # Iterate over the list and sum up the even indexed numbers
        even_index_sum += numbers[i]

    last_element = numbers[-1]   # Get the last element of the list
    result = even_index_sum * last_element  # Multiply the sum by the last element

print(f'Result: {result}')
