# Bool, None types
# Logic operators
# Зведення типів
# Duck typing
# If statement (programming golf, Тернарний оператор)
# list
# змінні не змінні типи даних різниця
# методи list(append(), pop(), sort(), copy())
# функція sorted()

# int
# float
# decimal
# complex

# string

# None
# bool
#
# list
# tuple
# set
# dict


############ NoneType ###########

# value = "hello"
#
# # value_id = id(value)
#
# value_print = print(value)
#
# print(value_print)

########## Boolean ############

# value = True


# value_int = -1
# value_float = 0.001
# value_string = ""
# print(bool(value_string))


# print(value * 2)

# value_int = 100
#
# print(bool(value_int) * 4)

# result = 1 + "1"
#
# print(result)


# value_1 = 15
# value_2 = 15.0

# print(value_1 != value_2)  # >, <, >=, <=, ==, !=, in, not, is(===)

# print("he" in "hello")
# print("he" not in "hello")

# print(value_1 == value_2)
# print(value_1 is value_2)


# if певна умова:
#   певну дію

# email = ""
#
# if not email:
# # if email == False:
#     print("Please add email")


# weather = "cold"
#
# if weather == "cold":
#     print("It's cold")
# else:
#     print("It's not cold")
#
# print("end")

# value_int = 12
#
# # and or
#
# if (value_int > 0) and (value_int < 10):                # 1
# # if 0 < value_int < 10:                                # 2
#     print(f"{value_int} is bigger than 0")
# elif value_int > 10:                             # else if
#     print(f"{value_int} is bigger than 10")
# else:
#     print(f"{value_int} is less than 0")



# not

# value_int = 12
#
# # and or
# not (A and B) = (not A) or (not B)   # почитай про бульову математику


# if not (value_int < 0) or not (value_int < 10):             # 1
# # if (value_int > 0) and (value_int < 10):                  # 2
# # if 0 < value_int < 10:                                    # 3
#     print(f"{value_int} is bigger than 0")
# elif value_int > 10:                             # else if
#     print(f"{value_int} is bigger than 10")
# else:
#     print(f"{value_int} is less than 0")



############ programming golf ############

# value = 0

# if value:
#     print("Hello")

# if value: print("hello")

# result = ""

# if value:
#     result = "Hello"
# else:
#     result = "end"
#
# print(result)

# result = 1 if value else 0
#
# print(result)

# value_int = 1
#
# if value_int > 0:     # 1
#     print(f"{value_int} is bigger than 0")
# elif value_int > 10:                             # else if
#     print(f"{value_int} is bigger than 10")
# else:
#     print(f"{value_int} is less than 0")




############### list ###########

# value_list = [1, 2.6, True, "Hello", [None, 2, 3]]    # від 0

# print(value_list, type(value_list))
# print(value_list[0])
# print(value_list[4][0])

# print(value_list[1:3]) # від включно, до виключно
# print(value_list[:3]) # від нульового до 3-го
# print(value_list[1:]) # від першого до останнього
# print(value_list[19:]) # не буде помилки


# print(value_list[::2])
# print(value_list[1::2])

# print(value_list[-1])


# print(value_list[::-1])


value_1 = 1
value_2 = 2
value_3 = None



value_list = [value_1, value_2, 10, [1, 2, 3], value_3] # [obj, obj, obj, link] ->  [obj, obj, obj]