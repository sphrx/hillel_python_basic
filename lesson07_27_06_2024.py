import string, keyword

# my_string = '__'  # Вивід: True
# my_string = 'x'  # Вивід: True
# my_string = 'get_value'  # Вивід: True
# my_string = 'get value'  # Вивід: False
# my_string = 'get!value'  # Вивід: False
# my_string = 'some_super_puper_value'  # Вивід: True
# my_string = 'Get_value'  # Вивід: False
# my_string = 'get_Value'  # Вивід: False
# my_string = 'getValue'  # Вивід: False
# my_string = '3m'  # Вивід: False

# result = True
#
# if my_string[0].isdigit() or my_string in keyword.kwlist:
#     result = False
#
# elif my_string.count("_") == len(my_string) and len(my_string) > 1:
#     result = False
# else:
#     for letter in my_string:
#         # if not result:
#         #     break
#         if letter == "_":
#             continue
#         elif letter.isupper():
#             result = False
#             break
#         elif (letter in string.punctuation or
#                 letter.isspace()):
#             result = False
#             break
#
#
# print(result)

# my_string = 'myString'  # Вивід: True
# result = False
#
#
# if my_string.count("_") == len(my_string) and len(my_string) > 1:
#     result = False
#
# if my_string in keyword.kwlist:
#     result = False
#
# if my_string.isidentifier():
#     if my_string == "_" or my_string.islower():
#         result = True
#
#
# print(result)

# num_1, _ = divmod()



# 'Python Community' -> #PythonCommunity
# 'i like python community!' -> #ILikePythonCommunity
# 'Should, I . subscribe? Yes!' -> #ShouldISubscribeYes

# user_text = input('Enter text: ').title()
#
# new_hashtag = '#'
#
# for symbol in user_text:
#     if symbol.isalnum():
#         new_hashtag += symbol
#
#
# print(new_hashtag[:140])


# s_cleaned = input_string.translate(str.maketrans('', '', string.punctuation))
# s_cleaned = ''.join([char for char in input_string if char not in string.punctuation])



# import string
#
# input_string = 'Should, I. subscribe? Yes!'.title()
# s_cleaned = input_string.translate(str.maketrans('', '', string.punctuation))
#
# print(s_cleaned)
#
# words = s_cleaned.split()
#
#
# # words_capitalized = [word.capitalize() for word in words]
#
# hashtag = '#' + ''.join(words)
#
# if len(hashtag) > 140:
#     hashtag = hashtag[:140]
#
# print(hashtag)

# def validation(num_1, num_2, action):
#     return True
#
# def adding(num_1, num_2):
#     return num_1 + num_2
#
# def sub(num_1, num_2):
#     return num_1 - num_2
#
# def dividing(num_1, num_2):
#     return num_1 / num_2
#
#
#
# def my_calc(num_1, num_2, action):
#     is_valid = validation(num_1, num_2, action)
#     if not is_valid:
#         result = "error"
#     elif action == "+":
#         result = adding(num_1, num_2)
#     elif action == "-":
#         result = sub(num_1, num_2)
#     if action == "/":
#         result = dividing(num_1, num_2)
#     else:
#         result = "error"
#
#     return result



# Modified calculator

# while True:
#     number_1 = input('Enter the first number: ')
#     if not number_1.isdigit():
#         print('Undefined number! Try again.')
#         continue
#     number_1 = float(number_1)
#
#     action = input('Enter the operator: ')
#     if action not in ('+', '-', '/', '*'):
#     # if action not in ['+', '-', '/', '*']:
#         print('Undefined operator! Try again.')
#         continue
#
#     number_2 = input('Enter the second number: ')
#     if not number_2.isdigit():
#         print('Undefined number! Try again.')
#         continue
#     number_2 = float(number_2)
#
#     result = 0
#
#     if action == '+':
#         result = number_1 + number_2
#     elif action == '-':
#         result = number_1 - number_2
#     elif action == '*':
#         result = number_1 * number_2
#     elif action == '/' and number_2 == 0:
#         result = str('Ділення на нуль неможливе!')
#     else:
#         result = number_1 / number_2
#
#     print(result)
#
#
#     var_cont = input('Do you want to stop? Y/N? ')  #Y y
#     if var_cont.lower() != 'y':
#         print('Good bye!')
#         break



# Множина (set)
#     Доступні методи
#     Порівняння множин
#     Frozenset


# my_set = set()
#
# print(my_set)


# my_list = [1, 2, 3, 4, 3, 2, 2, 1, 6]
# print(my_list)
#
# my_set = set(my_list)
# print(my_set)

# my_set = {1, 2, 3, 4, "apple", "yellow"}
# my_set_2 = {"red", "apple"}

# print(my_set)

# value_pop = my_set.pop()
# value_remove = my_set.remove("apple")
#
# print(value_remove)
# print(my_set)

# my_set.add("red")
# my_set.update(my_set_2)
#
# print(my_set)


# difference()
# intersection()
# union()


# my_set = {1, 2, 3, 4, "apple", "yellow"}
# my_set_2 = {"red", "apple"}

# my_set_3 = my_set.difference(my_set_2)  # my_set - my_set_2
# my_set_3 = my_set.intersection(my_set_2) # перетин все що є в обох сетах(множинах)
# my_set_3 = my_set.union(my_set_2) # перетин все що є в обох сетах(множинах)

# print(my_set_3)




# Frozenset

# my_set = {1, 2, 3, 4, "apple", "yellow"}
# my_set_2 = frozenset(my_set)
# print(my_set_2)




####################################### Functions ###################################################

# function vs method

# def my_formula():
#
#     result = 3 + 4
#
#     return result


# def get_set_update_edit_add_value():
#     pass
# def get_email_body():
#     pass
# def get_email_from_client():
#     pass



# def adding(num_1, num_2):
#
#     result = num_1 + num_2
#
#     if result < 0:
#         result = "error"
#
#     return result
#     # return None
#
#
#
#
#
# print(adding(1, 3))

# result = "Error"
# print(result)
#
#
# def adding(num_1, num_2):
#     res = num_1 + num_2
#     return res
#
#
#
# print(adding(1, 2))
# print(result)




# result = [1, 2, 3]
# print(result)
#
#
# def adding(num_1, num_2):
#     result.append(num_1+num_2)
#     return result
#
#
#
# print(adding(1, 3))
# print(result)


def correct_sentence(text):
    pass
# def correct_sentence(text):
#     """This func is doing something important"""







assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
# assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
# assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
# assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')