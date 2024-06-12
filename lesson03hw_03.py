original_list = []
if len(original_list) == 0:
    split_lists = [[], []]
else:
    middle_index = (len(original_list) + 1) // 2
    split_lists = [original_list[:middle_index], original_list[middle_index:]]
print(split_lists)

original_list = [1]
if len(original_list) == 0:
    split_lists = [[], []]
else:
    middle_index = (len(original_list) + 1) // 2
    split_lists = [original_list[:middle_index], original_list[middle_index:]]
print(split_lists)

original_list = [1, 2, 3, 4, 5]
if len(original_list) == 0:
    split_lists = [[], []]
else:
    middle_index = (len(original_list) + 1) // 2
    split_lists = [original_list[:middle_index], original_list[middle_index:]]
print(split_lists)

original_list = [1, 2, 3, 4, 5, 6]
if len(original_list) == 0:
    split_lists = [[], []]
else:
    middle_index = (len(original_list) + 1) // 2
    split_lists = [original_list[:middle_index], original_list[middle_index:]]
print(split_lists)
