# def add_one(some_list):
#     # all_nums = ''
#     # for number in some_list:
#     #     all_nums += str(number)
#     # added_1_int = int(all_nums) + 1
#     #
#     # result = []
#     # for i in str(added_1_int):
#     #     result.append(int(i))
#     #
#     # return result
#
#
#     # map()
#     added_1_int = int(''.join(map(str, some_list))) + 1
#     res = list(map(int, str(added_1_int)))
#     return res
#     #
#     #  list comprehension
#     # all_nums = ''.join([str(number) for number in some_list])
#     # added_1_int = int(all_nums) + 1
#     # return [int(num) for num in str(added_1_int)]
#
#
#
# assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
# assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
# assert add_one([0]) == [1], 'Test3'
# assert add_one([9]) == [1, 0], 'Test4'
# print("ОК")
import sys

# import string


# def is_palindrome(text):
#
#     # maketrnce('', '', string.punctuation)
#     # translate()
#
#     # new_text = ""
#     # for char in text:
#     #     if char.isalnum():
#     #         new_text += char.lower()
#
#     new_text = ''.join(char.lower() for char in text if char.isalnum())
#
#     return new_text == new_text[::-1]
#
#
# assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
# assert is_palindrome('0P') == False, 'Test2'
# assert is_palindrome('a.') == True, 'Test3'
# assert is_palindrome('aurora') == False, 'Test4'
#
# print("OK")







# def find_unique_value(some_list):
#     for value in set(some_list):
#         # unique_value = some_list.count(value)
#         if some_list.count(value) == 1:
#             return value
#
#
# assert find_unique_value([1, 1, 1, 1, 2]) == 2, 'Test1'
# assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
# assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
# print("ОК")


# def my_func():
#     """This func is doing something"""
#


# func = lambda x: x > 10





################## GENERATORS ###############

# import sys
#
# gen = range(1, 10)
#
# print(sys.getsizeof(gen))
# print(sys.getsizeof(list(gen)))



# def add_one(num):
#     return num + 1
#
#
# def count(start, func):
#     while True:
#         yield start
#
#         start = func(start)
#
#
# counter = count(0, add_one)
#
# print(counter)
#
# print(next(counter))
# print(next(counter))
#
# print("hello")
#
# print(next(counter))




# def s_gen():
#     x = 1
#     while x > 0:
#         print("Start Gen")
#         x = yield 45
#         print(f"Received {x}")
#         if x is None:
#             x = 0
#
# new_gen = s_gen()
#
# # print(new_gen)
#
# print(next(new_gen))
# # print(next(new_gen))
# new_gen.send(30)




# def add_one(num):
#     return num + 1
#
#
# def count(start, func):
#
#     while start < 10:
#         yield start
#
#         start = func(start)
#
#
# counter = count(0, add_one)
#
# print(list(counter))
# print(list(counter))


# list_compr = [i for i in range(1000)]
#
# list_gen = (i for i in range(1000))
#
# print(sys.getsizeof(list_compr))
# print(sys.getsizeof(list_gen))
# print(list_gen)
# print(next(list_gen))
# print(next(list_gen))
# print(next(list_gen))
# print(next(list_gen))




import time

# a = []
# start = time.time()
#
# for i in range(10_000_000):
#     a.append(i**2)
#
# end = time.time()
# print("for cicle t = ", end-start, " s")   # 0.6963839530944824
# # #
# start = time.time()
# b = [i**2 for i in range(10_000_000)]
# end = time.time()
# print("for generator list t = ", end-start, " s") # 0.40042591094970703
#
# start = time.time()
# c = (i**2 for i in range(10_000_000))
# end = time.time()
# print("for generator t = ", end-start, " s") # 0.0000021457672119140625
# # #
# start = time.time()
# c = list(c)
# end = time.time()
# print("for generator to list t = ", end-start, " s") # 0.5117743015289307












# Замикання (closures)

# def add(q, w):
#     return q + w
#
# a = add # Створення синоніму функції
# print(a(2, 3))




# """Область видимості параметра n належить до зовнішньої (охоплюючій) функції, проте
# вкладена функція може використовувати його. (LEGB)"""


# LEGB - local, enclosing, global, build-in

# def calculate_pow(n): # охоплююча функція
#     def calculate(number): # Вкладена функція
#         print(locals())
#         return number ** n # змінна з охоплюючої функції
#     return calculate # Возврат вложенной функции
#
# func = calculate_pow(3) # Виклик охоплюючої функції
# func_2 = calculate_pow(2) # Виклик охоплюючої функції
#
# # print(func) # покажчик на вкладену функцію
#
# number_one = func(2) # Виклик вкладеної функції
# # number_two = func_2(5)
# print(number_one)
# print(number_two)










# Використання модифікатора nonlocal
# first_number = 0
#
#
# def fibonacci():
#     second_number = 1
#     def get_next():
#         nonlocal second_number #оголошуємо змінну не локальною
#         global first_number
#         next_number = second_number + first_number
#         first_number = second_number
#         second_number = next_number
#         return next_number
#     return get_next










# Decorators





# my_function = []
#
# def add_function(func):
#     """
#     Функція приймає на вхід будь-який об'єкт (функцію), додає його до
#     списку my_function і повертає цей об'єкт.
#      """
#     my_function.append(func)
#     return func
#
# @add_function # Застосування створеної функції як декоратор
# def summ(x, y): # Декорована функція
#     return x + y
#
# @add_function
# def mul(x, y): # Декорована функція
#     return x * y

# print(my_function) # Список функцій, які ми задекорували

# print(mul) # функція працює так, як і було задумано
# print(mul(4, 5)) # функція працює так, як і було задумано


# # Створимо ще одну функцію і застосуємо до неї декоратор

# def div(q, w):
#     return q / w
# # # #
#
# div = add_function(div)

# @add_function
# def div(q, w):
#     return q / w
# #

# print(my_function)
#
# print(div(5, 6))




# Передача параметрів для функції, що декорується.

# def to_str(func):
#     #конструкція *args, **kwargs дозволяє приймати будь-які аргументи (позиційні та/або іменовані) та в будь-якій кількості
#     def get_str(*args, **kwargs): # Функція, яка приймає аргументи для функції, що декорується
#         """from any type to string"""
#         return str(func(*args, **kwargs))
#
#     return get_str # Як результат повертається інша функція
#
# @to_str
# def suma(x, y):
#     """I do nothing important"""
#     return x + y

# print("Summa = " + suma(3, 4)) # хоча функція suma повертає число, але тут помилка не виникне
# print(suma(3, 4), type(suma(3, 4))) # хоча функція suma повертає число, але тут помилка не виникне

# suma = to_str(suma)
# suma = get_str(*args, **kwargs) -> str(func(*args, **kwargs))

# print(suma) # бачимо вказівник на функцію get_str
# print(suma.__doc__) # бачимо вказівник на функцію get_str







# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     return inner
# #
# #
# @trace # identity = trace(identity)
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# #
# print(identity(50))
# #
# print(identity) # вказівник на функцію inner
# help(identity) # Help on function inner
# #
# print(identity.__name__, identity.__doc__) ## інформація з оригінальної функції



# встановимо "правильні" значення в атрибути функції, що декорується:
# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     # Встановлюємо для функції inner значення, які були у декорованої функції
#     inner.__module__ = func.__module__
#     inner.__name__ = func.__name__
#     inner.__doc__ = func.__doc__
#     return inner
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# print(identity.__name__, identity.__doc__) ##інформація з оригінальної функції



import functools
#
# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     functools.update_wrapper(inner, func)
#     return inner
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# print(identity.__name__, identity.__doc__)


# same with @wraps

# def trace(func):
#     """Декоратор trace виводить на екран повідомлення з
#          інформацією про виклик функції, що декорується"""
#     @functools.wraps(func)
#     def inner(*args, **kwargs):
#         """Inner doc"""
#         print(f'name: {func.__name__}, args: {args}, kwargs: {kwargs}')
#         return func(*args, **kwargs)
#     return inner
#
# @trace
# def identity(x):
#     """I do nothing useful."""
#     return x
#
# print(identity.__name__, identity.__doc__)
# print(identity(34))