



# import codecs
#
#
# def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:
#
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         html_code = file.read()
#
#     # cleaned_text = []
#     cleaned_text = ""
#     tag = False
#
#     for char in html_code:
#         if char == '<':
#             tag = True
#         elif char == '>':
#             tag = False
#         elif not tag:
#             # cleaned_text.append(char)
#             cleaned_text += char
#
#     # cleaned_text = ''.join(cleaned_text)
#     cleaned_text = '\n'.join(line.lstrip() for line in cleaned_text.splitlines() if line.strip())
#
#     with codecs.open(result_file, 'w', 'utf-8') as file:
#         file.write(cleaned_text)
#
#
# delete_html_tags('draft.html', 'cleaned.txt')



# from bs4 import BeautifulSoup
# import codecs
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#     with codecs.open(html_file, 'r', 'utf-8') as file:
#         soup = BeautifulSoup(file, 'html.parser')
#         text = soup.get_text(separator=' ').strip()
#
#     with open(result_file, 'w', encoding='utf-8') as result:
#         for line in text.split('\n'):
#             cleaned_line = line.strip()
#             if cleaned_line:
#                 result.write(cleaned_line + '\n')
#
#
# delete_html_tags("draft.html", "cleaned.txt")




# class Item:
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self):
#         return f"{self.name}, price: {self.price}. "
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name} {self.surname}"
#
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def get_total(self):
#         total = 99990
#         for key, cnt in self.products.items():
#             total += key.price * cnt
#         # self.total = 0
#         self.total = total  # 99990
#         return total
#
#     def __str__(self):
#         '''Метод виведення інформації про кошик'''
#         tmp = f'User: {self.user} \n'
#         for item, cnt in self.products.items():
#             tmp += f"Items:\n{str(item)}: {cnt} pcs. \n"
#         return tmp
#
#
# lemon = Item('lemon', 5, "yellow", "small", )
# apple = Item('apple', 2, "red", "middle", )
# # print(lemon)  # lemon, price: 5
#
#
# buyer = User("Ivan", "Ivanov", "02628162")
# # print(buyer)  # Ivan Ivanov
#
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 20 pcs.
# """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# """
# User: Ivan Ivanov
# Items:
# lemon: 4 pcs.
# apple: 10 pcs.
# """
# assert cart.get_total() == 40


################ Imports ###########

# import math
# from math import *

# from math import (
#     pi as PI,
#     acos,
# )

# from math import (
#     pi,
#     acos,
# )

# PI = math.pi
# PI = pi

# print(PI)










#1 Built-in (sys, time)
#2 Standard libreries (math, os, json, csv)
#3 Сторонні бібліотеки (pip)
#4 Створені в проекті модулі та пакети

# import math
# from lesson_12 import pow
#
# print(pow(5))

# from bs4 import BeautifulSoup
# #
# # print(sys.builtin_module_names)
#
# print(math.__name__)
# print(math.__doc__)
# print(math.__file__)








################ Поліморфізм ###########


# value_int = 1 + 2
# value_str = "1" + "2"
# # value_str = "1" + 2
#
# print(value_int)
# print(value_str)

# /,*, **, -, +

# __add__	__radd__	__iadd__	Складання чи конкатенація
# __sub__	__rsub__	__isub__	Віднімання
# __mul__	__rmul__	__imul__	Множення чи повторення
# __truediv__	__rtruediv__	__itruediv__	Справжній поділ
# __floordiv__	__rfloordiv__	__ifloordiv__	Поділ із округленням
# __mod__	__rmod__	__imod__	Розподіл по модулю
# __pow__	__rpow__	__ipow__	Зведення на ступінь





# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self, other):
#         # return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         return Box(self.x + other.x, self.y, self.z)
#
#     def __str__(self):
#         return f"Box [x = {self.x}, y = {self.y}, z = {self.z}]"
#
#
# box_a = Box(1, 2, 3)
# box_b = Box(2, 3, 4)
#
# # box_c = box_a + box_b
# # print(box_c)
#
# box_a += box_b
# # box_a += 1 # error
# #
# print(box_a)




# some_num = "10"
#
# if isinstance(some_num, str):
#     some_num = int(some_num)



# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         if isinstance(other, Box):
#             print("iadd")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         return NotImplemented
#
#     def __add__(self, other):
#         print(type(other))
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         return NotImplemented
#
#
# box_a = Box(1, 2, 3)
# box_b = Box(2, 3, 4)
# #
# box_a += box_b
# box_c = box_a + box_b

# box_a += 1 # error
# #
# print(box_a)
#
# box_c = box_a + box_b
# print(box_c)

# box_a += 1 # error


# box_d = box_a + 1 # TypeError говорить про те, що для даного типу операцій ми не маємо реалізації

# # Подібна помилка, коли ми спробуємо знайти суму числа та рядки
# 1 + '1'








# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __add__(self, other):
#         print("add")
#         if isinstance(other, Box):
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         if isinstance(other, (int, float)):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
# #
# #
# box_a = Box(1, 2, 3)
# # box_d = box_a + 10
# # print(box_d)
# box_e = 10 + box_a
# print(box_e)
# #
# # box_a += 20.0
# # print(box_a)



# box_d = 10.0 + box_a #  __radd__ not implemented
















# import numbers
#
#
# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __radd__(self, other):
#         """Оскільки метод __radd__ викликається у операнда, який знаходиться праворуч від знака +,
#         то self - це екземпляр класу Box,
#         а other - це операнд, який знаходиться ліворуч від знака +"""
#         print("radd")
#         return Box.__add__(self, other)
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         #  замість int, float перевіряємо приналежність до numbers.Real
#         if isinstance(other, numbers.Real):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
#
#     # помножити Box на число
#     def __mul__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x * other.x, self.y * other.y, self.z * other.z)
#         #  замість int, float перевіряємо приналежність до numbers.Real
#         if isinstance(other, numbers.Real):
#             return Box(self.x * other, self.y * other, self.z * other)
#         return NotImplemented
#
#
# box_a = Box(1, 2, 3)
# # box_d = box_a + 10
# # print(box_d)
# box_e = box_a * (10 + box_a)
# print(box_e)
#
# box_a += 20.0
# print(box_a)











# x.__eq__(y)	y.__eq__(x)	Рівне ==
# x.__ne__(y)	y.__ne__(x)	Не дорівнює
# x.__gt__(y)	y.__lt__(x)	x більше y
# x.__lt__(y)	y.__gt__(x)	x менше за y
# x.__ge__(y)	y.__le__(x)	x більше чи дорівнює y
# x.__le__(y)	y.__ge__(x)	x менше або дорівнює y

# import numbers
#
# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __iadd__(self, other):
#         return  Box.__add__(self, other)
#
#     def __radd__(self, other):
#         return  Box.__add__(self, other)
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         if isinstance(other, numbers.Real):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, numbers.Real):
#             return Box(self.x * other, self.y * other, self.z * other)
#         return NotImplemented
#
#     def volume(self):
#         return self.x * self.y * self.z
#
#     def __eq__(self, other):
#         if isinstance(other, Box):
#             # дві коробки вважаються рівними у разі рівності об'ємів
#             return self.volume() == other.volume()
#         return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, Box):
#             return self.volume() > other.volume()
#         return NotImplemented
#
#     # def __lt__(self, other):
#     #     #if isinstance(other, Box):
#     #        # return self.volume(self) < self.volume(other)
#     #     #return NotImplemented
#     #     return not self > other
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#
# box_a = Box(1, 2, 3)
# box_b = Box(3, 2, 1)
# print(box_a == box_b)
# # #
# box_c = box_a + box_b
# print(box_c == box_b)
# print(box_c > box_b)
# print(box_b < box_c)
# # # #
# print(box_c >= box_b) # TypeError немає реалізації методу більше або дорівнює








# class Box:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return "Box [x = {}, y = {}, z = {}]".format(self.x, self.y, self.z)
#
#     def __iadd__(self, other):
#         return Box.__add__(self, other)
#
#     def __radd__(self, other):
#         return Box.__add__(self, other)
#
#     def __add__(self, other):
#         if isinstance(other, Box):
#             print("add")
#             return Box(self.x + other.x, self.y + other.y, self.z + other.z)
#         if isinstance(other, numbers.Real):
#             return Box(self.x + other, self.y + other, self.z + other)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, numbers.Real):
#             return Box(self.x * other, self.y * other, self.z * other)
#         else:
#             return NotImplemented
#
#     @staticmethod
#     def volume(box):
#         return box.x * box.y * box.z
#
#     def __eq__(self, other):
#         if isinstance(other, Box):
#             return self.volume(self) == self.volume(other)
#         return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, Box):
#             return self.volume(self) > self.volume(other)
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Box):
#             return not self > other
#         return NotImplemented
#
#     def __ge__(self, other):
#         if isinstance(other, Box):
#             return any((self > other, self == other))
#         return NotImplemented
#
#     def __le__(self, other):
#         if isinstance(other, Box):
#             return any((self < other, self == other))
#         return NotImplemented
#
#     def __ne__(self, other):
#         return not self == other
#
# box_a = Box(1, 2, 3)
# box_b = Box(1, 2, 3)
# print(box_a >= box_b)
# box_c = box_a + box_b
# print(box_c >= box_b)
# print(box_a <= box_b)
# all([1, 0, True])
# any([1, 0, True])


# all()  # and
# any()  # or





# len()       __len__









########### Incapsulation #########


# Стандартна реалізація класу
# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         # self.color = color
#         self._color = color
#         # self.__color = color
#
#     @staticmethod
#     def get_voice():
#         return "Meow"
#
#     def _encrease_age(self, one):
#         self.age += one
#         # return self.age
#
#     def count_age(self, one):
#         age = self._encrease_age(one) # None
#         return self.age
#
#     # def buy_item(self):
#     #     self.item += 1
#     #     self._promo_code()
#     #     return "Theanks for purchasde"
#
#
#     def __str__(self):
#         msg = "Cat [ name = {}, age = {}, color ={}]"
#         return msg.format(self.name, self.age, self.color)
# # #
# cat = Cat('Barsik', 3, 'black')
# print(cat.get_voice())


# print(cat.color)
# cat.color = "green"
# print(cat.color)

# print(cat._color)
# cat._color = "green"
# print(cat._color)

# print(cat._Cat__color)
# cat._Cat__color = "green"
# print(cat._Cat__color)














# # Можна без особливих зусиль змінити значення поля
# cat.color = 'white'
# print(cat.color)


# def adding(num_1, num_2):
#     _res = num_1 + num_2
#     return _res



# barsik_dict = cat.__dict__
# print(barsik_dict)
# print(barsik_dict["name"])





# __dict__
# __slots__



class Cat:
    __slots__ = ("name", "age", "color")

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def __str__(self):
        msg = "Cat [ name = {}, age = {}, color = {}]"
        return msg.format(self.name, self.age, self.color)


cat_str = "Cat [ name = Barsic, age = 3, color = black]"
#
cat = Cat('Barsik', 3, 'black')
print(cat)
print(cat_str)
# # cat.type = "Simple cat"
# # print(cat.type)
# cat.name = "Tom"
# print(cat.name)








# Робота з методами __getattribute__, __getattr__, __setattr__ та __delattr__

# __getattribute__ - викликається автоматично при спробі набути значення певного або невизначеного (відсутнього) поля класу.
# __getattr__ - викликається автоматично при спробі отримати значення невизначеного поля класу.
# __setattr__ - викликається при спробі надати значення будь-якому полю класу (певного та невизначеного)
# __delattr__ – викликається при видаленні поля.