def correct_sentence(text: str) -> str:
    """
    A function that corrects the sentence by capitalizing the first letter and adding a period if missing.
    Parameters:
    text (str): The input text to be corrected.
    Returns:
    str: The corrected text with the first letter capitalized and ending with a period if needed.
    """
    return text[0].upper() + text[1:] if text.endswith('.') else text[0].upper() + text[1:] + '.'


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
