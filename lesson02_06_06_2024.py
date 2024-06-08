# Віртуальне середовище - навіщо його створювати та використовувати
# Змінні в Python
# Типи даних
# Цілі числа
# Арифметичні оператори
# Введення даних із клавіатури. Функція input()


#   comment win(ctrl + /)  mac(command + /)

# MONTH_IN_YEAR = 12
# NUMBER_PI = 3.14


# box = "apple"
# print(box)
#
# my_print = 3
#
# print(box)
# # first_box_number
#
# month_in_year = 12


################### Типи даних ###################

# змінні незмінні (мутабельні немутабельні)


# незмінні
# в незмінній зберігаємо обʼєкт(id обʼєкта)


# int       1
# complex   (1 + 2j)
# float     2.3333333334
# decimal   2.3333333333

# string     "hello 1 *)&"

# bool      True/False
# None

# tuple     () кортеж

# змінні
# в змінній зберігаємо посилання

# list      [] список/масив
# set       {} множина
# dict      {key: value} словник



# value_1 = 1
#
# value_2 = value_1
#
# print(value_2)    # 1
#
# value_1 = 2
#
# print(value_2)   # 1

# value_1 = True
# print(value_1, type(value_1), id(value_1))

# value_1 = 9
# value_2 = 2
#
# result_add = value_1 + value_2
# result_sub = value_1 - value_2
#
# result_div_1 = value_1 / value_2                # звжди флоат
# result_div_2 = value_1 // value_2               # цілочислене ділення
# result_div_3 = value_1 % value_2                # залишок від ділення
# result_div_4 = divmod(value_1,value_2)          # залишок від ділення
#
#
# result_mul = value_1 * value_2
# result_pow = value_1 ** value_2
# result_root = value_1 ** 0.5
#
# print(result_root, type(result_root))


########################## STRINGS ######################################

# value_str = "hello"
# value_str = 'hello'

# value_str = """hello"""
# value_str = '''hello'''

# value_str = """hello I'm Nick """

# print(value_str)

# value_str = 'hello I\'m Nick'  # екранування  \' \n \t \\
#
# print(value_str)

######## Конкотенація ########################################

# name = "Nick"
# age = 24
#
# # some_text = "Hi I'm " + name + ". " + "I'm " + str(age) + " " + "years old"               # 1
# some_text = f"Hi I'm {name}. I'm {age} years old"                                           # 2
#
# print(some_text)

########## input() ####################################  ALWAYS STRING

# name = input("Enter your name: ")
# age = input("Enter your age: ")
#
# next_year_age = int(age) + 1
#
# some_text = f"Hi I'm {name}. I'm {age} years old. Next year I'll be {next_year_age}"
#
# print(some_text)

# value_str = 4
# value_str = str(value_str)

# print(int(value_str), type(value_str))
# print(float(value_str), type(value_str))
# print(str(value_str), type(value_str))