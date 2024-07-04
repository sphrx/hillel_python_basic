def find_unique_value(some_list: list) -> int:
    """
    Find the unique value in the given list.

    The function takes a list of numbers and returns the unique value,
    which is the number that appears only once in the list.
    It is assumed that there is only one unique value in the list.

    :param some_list: A list of numbers.
    :return: The unique value in the list.
    """
    for value in some_list:
        if some_list.count(value) == 1:
            return value


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([2, 5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
assert find_unique_value([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]) == 2, 'Test4'
print("ОК")
