def is_palindrome(text: str) -> bool:
    """
    Check if the given text is a palindrome.

    A palindrome is a string that reads the same forward and backward,
    ignoring punctuation, whitespace, and letter case.

    :param text: The string to check for palindrome.
    :return: True if the text is a palindrome, False otherwise.
    """
    cleaned_text = ''.join(
        char for char in text.lower() if char.isalnum()
    )

    return cleaned_text == cleaned_text[::-1]


assert is_palindrome(
    'Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, '
    'Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, '
    'Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, '
    'Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, '
    'Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, '
    'Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, '
    'Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.'
)
assert not is_palindrome('0P')
assert is_palindrome('a.')
assert not is_palindrome('aurora')
print("ОК")
