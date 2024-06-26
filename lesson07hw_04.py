def common_elements() -> set:
    """
    Returns a set of common elements between two sets generated by list comprehension
    with a range of 0 to 100, filtering elements divisible by 3 and 5, respectively.
    """
    return {i for i in range(100) if i % 3 == 0}.intersection({i for i in range(100) if i % 5 == 0})


assert common_elements() == {0, 15, 30, 45, 60, 75, 90}

print(common_elements())
