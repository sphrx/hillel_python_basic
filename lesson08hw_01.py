def add_one(some_list: list) -> list:
    """
    This function takes a list of digits representing a number, adds 1 to that number,
    and returns a new list with the digits of the resulting sum.

    :param some_list: A list of digits representing a number.
    :return: A new list with the digits of the sum after adding 1 to the input number.
    """

    # Convert the list of digits to a number
    number = int(''.join(map(str, some_list)))

    # Increase the number by 1
    increased_number = number + 1

    # Convert the resulting number back to a list of digits
    result_list = list(map(int, str(increased_number)))

    return result_list


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
assert add_one([8, 2, 3, 4, 9]) == [8, 2, 3, 5, 0], 'Test5'
assert add_one([9, 9, 9, 9, 9]) == [1, 0, 0, 0, 0, 0], 'Test6'
print("OK")
