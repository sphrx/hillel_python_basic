new_lst = ['p', 'y', 't', 'h', 'o', 'n']

modified_lst = [new_lst[-1]] + new_lst[:-1] if len(new_lst) > 1 else new_lst

print(modified_lst)
#
# new_lst = []
# modified_lst= [new_lst[-1]] + new_lst[:-1] if len(new_lst) > 1 else new_lst
# print(modified_lst)  # Модифікований список: []
#
# new_lst = [2356]
# modified_lst = [new_lst[-1]] + new_lst[:-1] if len(new_lst) > 1 else new_lst
# print(modified_lst)  # Модифікований список: [1]
#
# new_lst = [11, 2, 55]
# modified_lst = [new_lst[-1]] + new_lst[:-1] if len(new_lst) > 1 else new_lst
# print(modified_lst)  # Модифікований список: [3, 1, 2]
#
# new_lst = ['p', 'y', 't', 'h', 'o', 'n'
# modified_lst = [new_lst[-1]] + new_lst[:-1] if len(new_lst) > 1 else new_lst
# print(modified_lst)
