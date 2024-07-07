def popular_words(text: str, words: list) -> dict:
    """
    Determine the popularity of specified words in a given text.

    :param text: Input text to search within.
    :param words: List of words to find in the text.
    :return: Dictionary with words as keys and their occurrence counts as values.
    """
    # Remove punctuation
    clean_text = ''.join(char for char in text if char.isalnum()
                         or char.isspace()).lower().split()

    return {word: clean_text.count(word) for word in words}


# Test with predefined example
assert popular_words(
    '''The proper function of man is to live, not to exist. 
    I shall not waste my days in trying to prolong them. I shall use my time.''',
    ['i', 'the', 'shall', 'exist']
) == {'i': 2, 'the': 1, 'shall': 2, 'exist': 1}

print('Test passed')



# input_text = input("Enter the text: ")
# input_words = input("Enter the words to search (comma-separated): ").split(',')

# input_words = [word.strip().lower() for word in input_words]
#
# result = popular_words(input_text, input_words)

# print(result)
