# def say_hi(name, age):
#     # return "Hi. My name is " + name + " and I'm " + str(age) + " years old"
#     # return "Hi. My name is {} and I'm {} years old".format(name, age)
#     # return "Hi. My name is Alex and I'm 32 years old"
#     return f"Hi. My name is {name} and I'm {age} years old"
#
#
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'say_hi error: text is not correct'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print("OK")


# def correct_sentence(text):
#
#     if text[0].islower():
#         text = text[0].upper() + text[1:]
#         # text = text.capitalize()
#
#     # if text[-1] != '.':
#     if not text.endswith('.'):
#         text += "."
#
#     return text
#
#
# assert correct_sentence("Greetings, friends") == "Greetings, friends.", 'correct_sentence error: check for dot'
# assert correct_sentence("hello.") == "Hello.", 'correct_sentence error: check for capital letter'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
# print('ОК')


# def second_index(text, some_str):
#     first_index = text.find(some_str)
#
#     if first_index == -1:
#         return None
#
#     seconds_index = text.find(some_str, first_index + len(some_str))
#
#     if seconds_index == -1:
#         return None
#
#     return seconds_index
#
#
# assert second_index("sims", "s") == 3, 'Test1'
# assert second_index("find the river", "e") == 12, 'Test2'
# assert second_index("hi", "h") is None, 'Test3'
# assert second_index("Hello, hello", "lo") == 10, 'Test4'
# print('ОК')


# def common_elements():
#     # multiples_of_3 = [num for num in range(100) if num % 3 == 0]
#     # multiples_of_5 = [num for num in range(100) if num % 5 == 0]
#
#     multiples_of_3 = {num for num in range(0, 100, 3)}
#     multiples_of_5 = {num for num in range(0, 100, 5)}
#
#     return multiples_of_3 & multiples_of_5
#
#     # return multiples_of_3.intersection(multiples_of_5)
#
#     # common_set = set(multiples_of_3).intersection(set(multiples_of_5))
#     # return common_set
#
#     # return set(multiples_of_3).intersection(set(multiples_of_5))
#
#     # return {num for num in range(0, 100, 3)} & {num for num in range(0, 100, 5)}
#
#
# assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
# print('ОК')


# Функції частина 3:
#
# Функція як параметр для іншої функції
# Документування функцій
# Анотування типів у функціях
# Рекурсія
# Анонімні функції lambda
# map, filter, zip
# Функції генератори yield


# def draw_rectangle(w, h, fill):
#     for i in range(h):
#         for j in range(w):
#             print(fill, end="")
#         print()
#
#
# # draw_rectangle(7, 5, "*")
#
# # *args **kwargs
#
# # payload = [7, 5, "*"]
# # payload = "75*"
#
# # payload = (7, 5, "*")
# payload = 7, 5, "*"
#
# draw_rectangle(*payload)


# def adding(num_1, num_2):
#     return num_1 + num_2
#
# def my_mul(num_1, num_2):
#     return num_1 * num_2
#
#
# # my_func = adding
# #
# # print(my_func(3, 3))
#
# my_list = [adding, my_mul]
#
# # print(my_list[0](1, 2))
# # print(my_list[1](1, 2))
#
# for func in my_list:
#     print(func(4, 2))

# choice = 0
#
# if choice == 1:
#     def my_calc(num_1, num_2):
#         return num_1 + num_2
# else:
#     def my_calc(num_1, num_2):
#         return num_1 / num_2
#
#
# print(my_calc(2, 3))


# def my_calc(num_1, num_2):
#     pass

# def my_calc_2(num_1, num_2):
#     """
#     This func is doing something!
#     Note: First arg ALWAYS STRING!
#     """
#     return num_1 + num_2


# my_calc()
# print(my_calc_2(1, 2))
# print(str.find())

######## Anotation


# def my_calc_2(num_1: int, num_2: int) -> int:
#     result = int(num_1) + int(num_2)
#     return result
#
#
# print(my_calc_2(1, 2))


# def my_calc_2(num_1, num_2):
#     """
#     This func is doing something!
#     Note: First arg ALWAYS STRING!
#     """
#     result = int(num_1) + int(num_2)
#     return result

# print(my_calc_2)
# print(my_calc_2.__name__)
# print(my_calc_2.__module__)
# print(my_calc_2.__doc__)

# if __name__ == "__main__":
#     pass


################################### Рекурсія ########################################################
#
# def fibo(n):
#     a = 0
#     b = 1
#
#     for i in range(2, n + 1):
#         a, b = b, a + b
#         # a = b
#         # b = a + b
#
#
#     return b
#
#
# print(fibo(10))
#
#
# def fibo(n):
#     if n in (1, 2):
#         return 1
#
#     return fibo(n - 1) + fibo(n - 2)
#
#
# print(fibo(10))


############ lambda ############ анонімна функція

# def bigger_that_zero(x):
#     return x > 0

# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result
#
#
# sequence = [1, 2, -4, 9]
# # print(my_filter(sequence, bigger_that_zero))
# # print(my_filter(sequence, lambda x: x > 0))
#
# bigger_that_zero = lambda x: x > 0
# # bigger_that_zero = lambda x: x % 2 == 0
# # bigger_that_zero = lambda x: x % 2 == 0 if x != 2 else False
#
# print(my_filter(sequence, bigger_that_zero))


# map() filter() zip()


# map()

# sequence = [1, 2, -4, 9]
#
# # value_list = []
# #
# # for num in sequence:
# #     value_list.append(str(num))
#
# value_list = map(str, sequence)
# # value_list = map(lambda x: x**2, sequence)
# # print(list(value_list))
# print(tuple(value_list))


# filter()

# def bigger_that_zero(x):
#     return x > 0
#
# def my_filter(seq, predicate):
#     result = []
#
#     for el in seq:
#         if predicate(el):
#             result.append(el)
#
#     return result

# sequence = [1, 2, -4, 9]
#
# # result = my_filter(sequence, bigger_that_zero)
# result = filter(lambda x: x > 0, sequence)
#
# print(list(result))


# zip()


# my_list_1 = [1, 2, 3, 4]
# my_list_2 = ["apple", "banana", "black", "red"]
# my_list_3 = [False, True]

# for i in zip(my_list_1, my_list_2, my_list_3):
#     print(i)

# for i in range(2):
#     print(tuple([my_list_1[i], my_list_2[i], my_list_3[i]]))



###########   Generators   ####################

import sys

# gen = range(10)
# gen_list = list(gen)

# print(gen)
# print(sys.getsizeof(gen))
#
# print(list(gen))
# print(sys.getsizeof(list(gen)))


# for i in range(10):
#     print("Hello")
#
# for i in gen_list:   # не правильно!
#     print("Hello")


def add_one(num):
    return num + 1


def count(start, func):
    while True:
        yield start
        start = func(start)
        # yield start




counter = count(0, add_one)

print(counter)

print(next(counter))
print(next(counter))

print("hello")

print(next(counter))