import codecs


def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
    """
    Remove HTML tags from the specified file and write the cleaned text to another file.

    Args:
        html_file (str): The name of the file to clean.
        result_file (str): The name of the file to write the cleaned text. Default is 'cleaned.txt'.
    """
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html_code = file.read()

    cleaned_text = []
    tag = False

    for char in html_code:
        if char == '<':
            tag = True
        elif char == '>':
            tag = False
        elif not tag:
            cleaned_text.append(char)

    cleaned_text = ''.join(cleaned_text)
    cleaned_text = '\n'.join(line.lstrip() for line in cleaned_text.splitlines() if line.strip())

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(cleaned_text)


delete_html_tags('draft.html', 'cleaned.txt')
