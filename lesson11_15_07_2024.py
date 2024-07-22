# text = "When I was One I had just begun When I was Two I was nearly new"
# words = ['i', 'was', 'three', 'near']

# L(local)E(enclosing)G(global)B(built-in)


# def popular_words(txt, wrds):
#     text_words = txt.lower().split()
#     return {word: text_words.count(word) for word in wrds}
#
#
#     # popular_dict_words = {word: 0 for word in words}
#
#     # for word in text_words:
#     #     if word in words:
#     #         popular_dict_words[word] = text_words.count(word)
#
#
#
#     # popular_dict_words = {}
#     #
#     # for word in words:
#     #     popular_dict_words[word] = text_words.count(word)
#     #
#     # return popular_dict_words
#
#
#
#     # return {word: text_words.count(word) for word in words}
#
#
# print(popular_words(text, words))
#
# assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
# print('OK')











# def difference(*numb_args):
#     if not numb_args:
#         result = 0
#     else:
#         result = max(numb_args) - min(numb_args)
#         result = round(result, 2)
#
#     return result


# def difference(*numb_args):
#     if not numb_args:
#         return 0
#
#     result = max(numb_args) - min(numb_args)
#     return round(result, 2)


# def difference(*numb_args):
#     if numb_args:
#         result = max(numb_args) - min(numb_args)
#         return round(result, 2)
#
#     return 0
#
#
#
# print(difference(5, -5))
#
# assert difference(1, 2, 3) == 2, 'Test1'
# assert difference(5, -5) == 10, 'Test2'
# assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
# assert difference() == 0, 'Test4'
# print('OK')




#################### ФАЙЛИ ##################

# filename = "test_text.txt"
# my_file = open(filename, "w")   # "w", "r", "a", "x"

# write
#
# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
# my_file.write("Hello World!\n")
# my_file.write("Hello World!")
# #
# my_file.close()



# with open(filename, "w") as my_file:
#     my_file.write("Hello World!\n")





# writelines

# val_list = ["Hello\n", "red\n", "green\n", "yellow\n"]
#
# my_file.writelines(val_list)
# for i in val_list:
#     my_file.writelines(i + "\n")

# my_file.close()

# with open(filename, "w") as my_file:
#     my_file.writelines(val_list)



####### read ########


filename = "test_text.txt"

# my_file = open(filename, "r")   # "w", "r", "a", "x"
#
# data = my_file.read()
#
# my_file.close()
#
# print(data, type(data))

# with open(filename, "r") as my_file:
#     data = my_file.read()
#
# print(data, type(data))

####### readlines ########

# with open(filename, "r") as my_file:
#     data = my_file.readlines()
#
# print(data, type(data))


####### readline ########

# with open(filename, "r") as my_file:
#     print(my_file.readline())
#     print(my_file.readline())

# print(data, type(data))


############# a add #########

# with open(filename, "a") as my_file:
#     # my_file.write("gggggg!!!!!!!!\n")
#     data = my_file.write("gggggg!!!!!!!!\n")
#
# print(data)

# with open(filename, "a+") as my_file:
#     # my_file.write("gggggg!!!!!!!!\n")
#     data = my_file.write("gggggg!!!!!!!!\n")
#     my_file.seek(4)
#     ctx = my_file.read(20)
#
# print(ctx)


#
# with open(filename, "rb") as my_file:
#     print(my_file.readline())
#



# with open(filename, "r", encoding="UTF-8") as my_file:
#     data = my_file.readlines()
#
# print(data, type(data))




################## OOP ############

# class

# class Car:
#     """Some doc string"""
#     color = "green"        # атрибут
#     engine = 2.0
#
# car_1 = Car()        # екземпляр(instance)/обʼєкт
# car_2 = Car()
# print(car_1)
# print(car_1.engine)
# print(car_1.color)
# car_1.color = "red"
# print(car_1.color)
# car_1.van = "sedan"     # атрибут екземпляру класу
# print(car_1.van)



value_str = "hello"

print(type(value_str))