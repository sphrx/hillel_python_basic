# str
# str methods(lower, upper, capitalize, isalpha, rfind, replace, startwith)


# first_symbol = float(input("1st num:  "))
# operator = input("please tipe an operator(can work with +, -, *, /):  ")
# second_symbol = float(input("2nd num:  "))
#
# # result = "ERROR - Invalid symbol"
# # result = 0
# # result = None
#
# # if operator == "+" or operator == "-" or operator == "*" or operator == "/":
# # if operator not in "+-*/":
# # if operator not in "+-*/" or len(operator) > 1:
# # if operator not in ["+", "-", "*", "/"]:
# if operator not in ("+", "-", "*", "/"):
#     result = "ERROR - Invalid symbol"
# elif operator == "+":
#     result = first_symbol + second_symbol
# elif operator == "-":
#     result = first_symbol - second_symbol
# elif operator == "*":
#     result = first_symbol * second_symbol
# elif operator == "/" and second_symbol == 0:
#     result = "ERROR - can't divide by zero"
# # elif operator == "/" and second_symbol != 0:
# elif operator == "/":
#     result = first_symbol / second_symbol
# # else:
# #     result = "ERROR - Invalid symbol"
#
# print(result)


# original_list = [12, 5, 6, 7, 8]
#
# if len(original_list) > 1:
#     last_element = original_list.pop()
#     original_list.insert(0, last_element)
#
# # if len(original_list) > 0:
# #     original_list.insert(0, original_list[-1])
# #     original_list.pop()
#
# print(original_list)
#


# my_list = [1, 2, 3, 9, 4, 5, 6]
#
# separator = len(my_list) - len(my_list) // 2
# new_list = [my_list[:separator], my_list[separator:]]
#
# print(new_list)


##################### String ##############

# value_str = "Hello"
#
# print(value_str, id(value_str))
#
# value_str = "Hello!"
#
# print(value_str, id(value_str))

# value_email = "emAil@Gmail.com"
# # value_email = "Email@gmail.com"
# value_name = "nick NICK"

# print(value_name[0])
# print(value_name[0:6])
# print(value_name[:])

# print(value_email)
# value_upper = value_email.upper()
# value_lower = value_email.lower()
# value_capital = value_name.capitalize()
# value_title = value_name.title()
# value_swap = value_name.swapcase()

# print(value_swap)
# print(value_title)
# # print(value_upper)
# # print(value_lower)
# print(value_capital)

# value_name = "_____Nick_______"

# strip()
# print(value_name)

# value_strip = value_name.strip()
# value_strip = value_name.strip("_")
# value_strip = value_name.rstrip("_")
# value_strip = value_name.lstrip("_")


# print(value_strip)

# value_int = "12h;;;jgh   gjue444"
# new_val = ""
# # print(value_int.isdigit())
# # print(value_int.isalpha())
#
# for symb in value_int:
#     if not symb.isdigit():
#         # if symb.isalpha():
#         new_val += symb
#
# print(new_val)
#
#
# print(value_int, type(value_int))
# print(float(value_int))


################## find/rfind ######################

# value_str = "Helloollkkkkkkkkkllllllllkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"

# print(value_str.find("l"))
# print(value_str.rfind("l"))

# print(value_str.find("2"))
# print(value_str.index("2"))

# count = 0
#
# for letter in value_str:
#     if letter == "l":
#         count += 1
#
# print(count)


# count = 0
#
# while found_index != -1:
#     count += 1
#     found_index = value_str.find(value_str, found_index + 1)
#

# print(value_str.count("l"))


############ split() rsplit() join() ####################

# value = "name.png"
# value = "C/Document/folder/name.png"

# value_list = value.split("/", 1)
# value_list = value.rsplit("/", 1)


# value_list = value.split("/")
# print(value_list)
#
# new_val_str = "\\".join(value_list)
# print(new_val_str)

# value_list = value.rsplit(".", 1)
#
# value_list[1] = "jpeg"
# print(value_list)
# new_val_str = ".".join(value_list)
# print(new_val_str)


# replace()
# value = "C/Document/folder/j4kji_4.png"


# print(value)
#
# new_value = value.replace(".png", ".jpeg")
#
# print(new_value)


# startswith()
# endswith()

# value_str = "hello"
# print(value_str.startswith("he"))
# print(value_str.endswith("o"))


########### ASCII ########### стандарт кодування

# letter = "d"
######### ord()
# print(ord(letter))
#
# address = 100
# print(chr(address))
#
# import this
#
# print(this)

# alphabet = ""
#
# for letter in range(ord("A"), ord("z") + 1):
#     alphabet += chr(letter)
#
# print(alphabet)


# print(alphabet)