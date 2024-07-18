def is_even(number: int) -> bool:
    """
    Перевіряє, чи є число парним без використання операцій ділення.

    Ця функція використовує побітову операцію AND для перевірки
    останнього біта числа. Якщо останній біт дорівнює 0, число парне,
    інакше - непарне.
    """
    return (number & 1) == 0


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("Ok!")
