def difference(*args):
    """
    Finds the difference between the maximum and minimum values in a set of numbers.

    :param args: Variable number of arguments (int or float)
    :return: Difference between the maximum and minimum (int or float)
    """
    return round(max(args) - min(args), 2) if args else 0


# Tests
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test5'
print('Test passed')

# # Interactive input
# "Enter numbers separated by spaces (press Enter when done):"
# user_input = input("Enter numbers separated by spaces (press Enter when done): ")
# numbers = [float(num) for num in user_input.split()]
#
# result = difference(*numbers)
# print(f"The difference between the maximum and minimum values is: {result}")
