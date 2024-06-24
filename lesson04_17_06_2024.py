# match/case
# list
# while
# break and continue
# while - else
# for
# for - else
# range()


# my_input = int(input("Please write 4-digit number: "))
#
# thousands = my_input // 1000
# hundreds = my_input // 100 % 10
# tenth = my_input // 10 % 10
# ones = my_input % 10
#
# print(f"{thousands}\n{hundreds}\n{tenth}\n{ones}")
# print(hundreds)
# print(tenth)
# print(ones)





# my_input = int(input("please add 4 digits: "))
#
# thousands, left_1 = divmod(my_input, 1000)
# hundreds, left_2 = divmod(left_1, 100)
# tens, ones = divmod(left_2, 10)
#
# print(thousands)
# print(hundreds)
# print(tens)
# print(ones)







# num = divmod(input, 1000)

# num_1, num_2, *temp = [1, 2, 8, 9]
# print(num_1)
# print(num_2)
# print(temp)
#
# num_1 = 5
# num_2 = 10
#
# num_1, num_2 = num_2, num_1



# print(num[0])
# print(num[1])




# entered_num = int(input("Enter your number: "))

# first_num = entered_num % 10 * 10000
# second_num = entered_num % 100 // 10 * 1000
# third_num = entered_num % 1000 // 100 * 100
# fourth_num = entered_num % 10000 // 1000 * 10
# fifth_num = entered_num % 100000 // 10000

# first_num = entered_num % 10
# second_num = entered_num % 100 // 10
# third_num = entered_num % 1000 // 100
# fourth_num = entered_num % 10000 // 1000
# fifth_num = entered_num % 100000 // 10000
#
#
# print(first_num, second_num, third_num, fourth_num, fifth_num, sep=',')
# print(second_num)
# print(third_num)
# print(fourth_num)
# print(fifth_num)
#
# print(first_num + second_num + third_num + fourth_num + fifth_num)




# match/case
# list
# while
# break and continue
# while - else
# for
# for - else
# range()


# operator = ""
#
# # if operator == "+" or "-":
# if (operator == "+") or (operator == "-"):
#     print("!!!!!!!")
# else:
#     print("?????")
#
# print("end")




# match/case

# weather = "llll"
#
# match weather:
#     case "cold":
#         print("cold")
#     case "hot":
#         print("hot")
#     case _:
#         print("no weather")


###################### list ######################


# ############################################

# base_list = [1, 2, 3]
# my_new_list = base_list * 4
# print(my_new_list)
#
# # my_new_list[obj, obj, obj, obj, obj, obj, obj, obj, obj, obj, obj, obj,]
#
# base_list[0] = 10
#
# print(f"base_list {base_list}")
# print(f"my_new_list {my_new_list}")

# # # ######################################

# from copy import deepcopy


# base_list = [1, 2, 3, ["hello", True]]
# my_new_list = [base_list] * 4
# my_new_list = [base_list.copy()] * 4
# my_new_list = [deepcopy(base_list)] * 4
# print(my_new_list)

# my_new_list = [link, link, link, link]


# base_list[-1][0] = False
# print(f"base_list {base_list}")
# print(f"my_new_list {my_new_list}")

# value_list = [1, 2, 3] # 88 byte
#
# value_list.append(4)  # 88 byte
# value_list.append(4)  # 88 byte
# value_list.append(4)  # 122 byte
# value_list.append(4)  # 122 byte


# value_list = [1, 2, 3]
# print(value_list)
# value_list.append(1)
# value_list.insert(4,"4")
# print(value_list)
#
# value_list.insert(4,"5")
# print(value_list)
#
# value_list.insert(4,"6")
# print(value_list)
#
# value_list.insert(4,"7")
# print(value_list)

# value_pop = value_list.pop(1)
# print(value_pop)
# print(value_list)

#
# value_list = [1, "Hello", 2, 3, "Hello"]
# print(value_list)
#
# value_list.remove("Hello")
# print(value_list)

# reverse()

# value_list = [1, "Hello", 2, 3, "Hello", True]
# print(value_list)
#
# value_list.reverse()
# print(value_list)

################# sort / sorted() #################


# value_list = [1, 2, 27, 3, 45, True]
# # value_list = ["hello", "red", "yellow", "aapple", "pig", "apple", ""]    # ASCII
# # value_list = ["hello", "red", 1, "yellow", 2, "aapple", "pig", "apple"]
# # print(value_list)
# #
# # # value_list.sort(key=len)
# value_list.sort()
# # print(value_list)
#
# # value_list.sort(reverse=True, key=bool)
# print(value_list)
#
# value_list = [[1, 2, 3], [4, 56, 6], [2, 8]]

# # value_list = sorted(value_list, reverse=True, key=)
# value_list = sorted(value_list, key=len)
# print(value_list)



# while
# # break and continue
# # while - else


########## цикл loop ############
#
# count = 0
# is_true = True

# while True:
#     count += 1
#     print(count)
#     if count >= 10:
#         break


# while is_true:
#     if count >= 10:
#         is_true = False
#     count += 1
#     print(count)

# while count < 10:
#
#     count += 1
#     # if count % 2:
#     #     continue
#     if count == 5:
#         break
#     print(count)
# else:
#     print("else")
#
# # break
# # continue
#
#
# print("end")




# for
# for - else
# range()


############### for ################


value_list = [1, 2, 3, True, 6, 7, 9]
# count = 0
# while count < len(value_list):
#     print(value_list[count])
#     count +=1


# for num in value_list:
#     print(num)
#
#
# print("end")

# range()
# range(5) до
# range(1, 5) від до
# range(1, 5, 2)  від до крок


for index in range(1, 10, 2):
    if index == 5:
        # break
        continue
    print(index)
else:
    print("else")

# for index in range(len(value_list)):
#     print(value_list[index], index)