# tuple
# змінна "_"
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())


# my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# second_list = []
#
# zero = my_list.count(0)
#
# for index in range(len(my_list)):
#     if my_list[index] != 0:
#         second_list.append(my_list[index])
#
# second_list.extend([0] * zero)
#
# print(second_list)



# my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
#
# for index in range(len(my_list)):
#     if my_list[index] == 0:
#         my_list.remove(0)
#         my_list.append(0)
#
#
# print(my_list)

import operator

# my_list = [0, 9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

# my_list.sort(key=operator.not_)
# my_list.sort(reverse=True, key=bool)
#
# print(my_list)
# print(sorted(my_list, reverse=True, key=bool))





# my_list = [0, 1, 7, 2, 4, 8]
#
# result = 0
#
# # for i in range(0, len(my_list), 2):
# #     result += my_list[i]
# #
# # if my_list != []:
# #     result = result * my_list[-1]
#
# # if my_list != []:
# if my_list:
#     result = sum(my_list[::2]) * my_list[-1]
#
# print(result)




# import random

# my_list = random.sample(range(1, 100), random.randint(3, 10))
# count = random.randint(3, 10)

# my_list = []
# for i in range(count):
#     my_list.append(random.randint(1,100))

# my_list = [random.randint(1,100) for i in range(count)]
# my_list = [random.randint(1,100)**2 for i in range(count) if i % 2]

# print(my_list)


# if len(my_list) >= 3:
# new_list = [my_list[0], my_list[2], my_list[-2]]
# print(new_list)
# else:
#     print('not enough elements in list')





# змінна "_"
# tuple
# поняття dict
# основні методи dict(update(), get(), pop(), keys(), values(), items())


###################### змінна "_" ######################

# _ = "hello"

# coordinates = (10, 20)
#
# value_1, _ = coordinates
# print(value_1)

# for _ in range(3):
#     print("hello")


################# tuple ################ нeзмінний

# my_list = [
#     1,
#     2,
#     3,
#     4,
# ]
#
# my_tuple = (
#     1,
#     2,
#     3,
#     4,
# )
#
# print(my_list, type(my_list))
# print(my_tuple, type(my_tuple))



# some_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# print('some_tuple =', some_tuple.__sizeof__())
# print('some_list =', some_list.__sizeof__())

# some_tuple = (1, 2, 3, [5, 6])
# print(some_tuple)
#
# some_tuple[-1].append(True)
# print(some_tuple)



############ dict ################# словник       ключ:значення

# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
#     1: 10,
#     1.5: "jjj",
#     True: "kkkk",
#     None: "kkkk",
#     (10, 10, 99): "blue",
#     # [1, 2, 3]: "kkkk"
# }

# "rgb"

# print(my_dict)
#
# print(hash("name"))
# print(hash(100))
# print(hash(1.5))


# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }

# print(my_dict)
# print(my_dict["name"])

# my_dict["name"] = "Nikolas"
# my_dict["name_2"] = "John"
# print(my_dict["name"])
# print(my_dict["name_2"])

# email = my_dict.get("email", False)
#
# if not email:
#     print("email is a mandatory field")
#
# print(email)
# print(my_dict)

# update()

# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
#
#
# my_dict["name"] = "Nikolas"
# my_dict.update({"name": "Nikolas"})
# print(my_dict)

# pop()

# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
# #
# value_pop = my_dict.pop("name")
#
# print(value_pop)
# print(my_dict)


# popitem()
# value_pop = my_dict.popitem()
#
# print(value_pop)
# print(my_dict)


# fromkeys()

# some_dict = dict.fromkeys(("name", "age", "country"), False)
# # some_dict = dict.fromkeys(("name", "age", "country"), []) # краще так не робити
#
# print(some_dict)
#
# some_dict["name"].append(9)
# print(some_dict)


# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
#
# # print(my_dict["name"], my_dict["age"])
# print(my_dict)





# for key in my_dict:
#     print(key, my_dict[key])

# for key in my_dict.keys():
#     print(key, my_dict[key])

# for value in my_dict.values():
#     print(value)

# for key, value in my_dict.items():
#     print(key, value)



# my_list = ["Hello", "Apple", "Red"]
# for i in enumerate(my_list):
#     print(i)


# my_dict = {
#     "name": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
#
# my_dict = {
#     "name_2": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }

# my_new_dict = my_dict + my_dict_2

# print(my_new_dict)

#
# print(list(my_dict.keys()))
# print(list(my_dict.values()))
# print(list(my_dict.items()))



# my_list = [random.randint(1,100) for i in range(count)]

# my_dict = {num: [1] for num in range(5)}
# print(my_dict)


# OrderedDict

from collections import OrderedDict, defaultdict

# my_dict = {
#     "name_2": "Nick",
#     "age": 18,
#     "country": "Ukraine",
# }
#
# print(my_dict)
#
# my_dict_ord = OrderedDict(my_dict)      # [('name_2', 'Nick'), ('age', 18), ('country', 'Ukraine')]
#
# print(my_dict_ord)



# defaultdict vs fromkeys()

# some_dict = dict.fromkeys(("name", "age", "country"), False)

# new_dict = defaultdict(list)
#
# for i in range(5):
#     new_dict[i].append(i * 5)
#
# print(new_dict)

from collections import namedtuple

# fields = ("color", "engine")
#
# car = namedtuple("Car", fields)
#
# car_1 = car("red", 2000)
#
# print(car_1)
# print(car_1.color)
# print(car_1.engine)