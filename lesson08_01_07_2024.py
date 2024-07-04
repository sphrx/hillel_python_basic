# Глобальні та локальні змінні.
# Передача аргументів.
# Правило доступу до змінних LEGB
# Використання іменованих параметрів.
# аргументи за замовчуванням
# Використання змінної кількості аргументів
# Використання змінної кількості іменованих аргументів
# Тонкощі використання аргументів
# Розпакування кортежу в низку фактичних параметрів
# Розпакування словника в низку фактичних параметрів
# Особливості використання функцій


# import string
#
# input_str = input('Enter two letters hyphenated: ').split('-')  # a-c -> ["a", "c"]
#
#
# beginning = string.ascii_letters.find(input_str[0])
# ending = string.ascii_letters.find(input_str[-1])
#
# if beginning == -1 or ending == -1:
#     print("error")
# else:
#     print(string.ascii_letters[beginning:ending + 1])

# beginning = string.ascii_letters.index(input_str[0])
# ending = string.ascii_letters.index(input_str[-1])


# min()
# max()


#
# conditions_1 = ('11', '12', '13', '14')
# conditions_2 = ('0', '5', '6', '7', '8', '9')
# conditions_3 = ('2', '3', '4')


# total_seconds = int(input("Введіть кількість секунд (від 0 до 8639999): "))
#
# if 0 <= total_seconds < 8640000:
#     days, seconds_left = divmod(total_seconds, 86400)
#     hours, seconds_left = divmod(seconds_left, 3600)
#     minutes, seconds = divmod(seconds_left, 60)

#     if days % 10 == 1 and days % 100 != 11:
#         day_word = "день"
#     elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
#     # elif 2 <= days % 10 <= 4:
#     #     if days % 100 < 10 or days % 100 >= 20:
#             day_word = "дні"
#     else:
#         day_word = "днів"
#
#     print(f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}")
# else:
#     print("Введене число повинно бути від 0 до 8639999.")


# number = int(input("Enter number: "))  #999
#
# result = 1
#
# while number > 9:
#     for digit in str(number):
#         result *= int(digit)
#     number = result  # після першого кроку 729
#     result = 1
#
# print(number)


# result = eval("2 * 9")
# print(result, type(result))


# number = int(input("Enter number: ")) or 1
#
# while number > 9:
#     number = eval('*'.join(str(number)))  #"9*9*9"
#
# print(number)


# Глобальні та локальні змінні.
# Передача аргументів.
# Правило доступу до змінних LEGB
# Використання іменованих параметрів.
# аргументи за замовчуванням
# Використання змінної кількості аргументів
# Використання змінної кількості іменованих аргументів
# Тонкощі використання аргументів
# Розпакування кортежу в низку фактичних параметрів
# Розпакування словника в низку фактичних параметрів
# Особливості використання функцій


# LEGB правила доступу до змінних

# result = 500
#
# print(result)
#
#
# def adding(num_1, num_2):
#
#     result = num_1 + num_2
#
#     return result
#
#
# print(result)
#
# print(adding(1, 2))
#
# print(result)

# from math import pi
#
# pi = "global"
#
# def outer():
#     pi = "enclosing"
#     def inner():
#         pi = "local"
#         print(pi)
#
#     inner()
#
# outer()


# from math import pi

# pi = "global"
# CORS_ALLOW = ("www.google.com", "instagram.com")
#
# def outer():
#     # pi = "enclosing"
#     def inner():
#         # pi = "local"
#         pi += "!!!!!"
#         print(pi)
#
#     inner()
#
# outer()


# import operator
#
# actions = {
#     "+": operator.add,
#     "-": operator.sub,
#     "*": operator.mul,
#     "/": operator.truediv,
# }
#
# num_1 = float(input())
# num_2 = float(input())
# action = input()
#
# func = actions.get(action)
#
# if not func:
#     print("error")
# else:
#     print(func(num_1, num_2))


# def say_hi(name):
#     print(f"Hi! {name}")
#     return None

# def say_age(age):
#     print(f"You are {age} years old")
#     return None
#
#
# def print_line(w, fill="&", name=None, age=None):
#     for i in range(w):
#         print(fill, end="")
#
#     if name:
#         say_hi(name)
#
#     if age:
#         say_age(age)
#
#
#     return None
#
# # print_line(16, "*")
# # print_line(fill="*", w=16)
# # print_line(16, fill="*")
#
# print_line(16, "*", "Nick", 18)


# args kwargs


# value_tuple = (1, 2, 3, 4, 5, 6)
# val_1, val_2, *tmp = value_tuple
#
# print(val_1)
# print(val_2)
# print(tmp)

# def teachers_group(*args):
#     group_dict = {
#         "teacher": "Nick",
#         "group_list": list(args)
#     }
#     # for i in args:
#     #     group_dict["group_list"].append(i)
#
#     return group_dict
#
# print(teachers_group("John", "Bob", "Jessy"))


# kwargs



def say_hi(name):
    print(f"Hi! {name}")
    return None

def say_age(age):
    print(f"You are {age} years old")
    return None


# def print_line(w, fill="&", name=None, age=None):
def print_line(w, fill="&", **kwargs):

    print(kwargs)

    for i in range(w):
        print(fill, end="")

    if kwargs.get("name"):
        say_hi(kwargs.get("name"))

    if kwargs.get("age"):
        say_age(kwargs.get("name"))


    return None

# print_line(16, "*")
# print_line(fill="*", w=16, name="Nick", age_2=19)
print_line(16, fill="*", name=False)