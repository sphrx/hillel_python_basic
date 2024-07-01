def second_index(text: str, some_str: str) -> int or None:
    """
    Find the second occurrence of a substring in a given text.
    Args:
        text (str): The input text to search for the substring.
        some_str (str): The substring to search for.
    Returns:
        int or None: The index of the second occurrence of the substring in the text,
        or None if the substring is not found or occurs only once.
    """
    return text.find(some_str, text.find(some_str) + 1) if text.count(some_str) > 1 else None


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
