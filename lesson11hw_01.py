from inspect import isgenerator


def prime_generator(end: int):
    """
    Генерує послідовність простих чисел до заданої межі (включно).

    Ця функція використовує просту перевірку дільників для визначення
    простих чисел. Вона перевіряє всі числа від 2 до заданої межі
    і повертає ті, які є простими.
    """
    for num in range(2, end + 1):
        if all(num % i for i in range(2, int(num ** 0.5) + 1)):
            yield num


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok!')
