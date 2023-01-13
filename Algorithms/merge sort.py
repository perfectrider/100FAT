
a = [5, 3, -2, 12, 355, 7, 8, 3, 4]

def sort_and_merge(list1, list2):
    merged_array = []

    x = 0
    y = 0
    while x < len(list1) and y < len(list2):
        if list1[x] <= list2[y]:
            merged_array.append(list1[x])
            x += 1
        else:
            merged_array.append(list2[y])
            y += 1

    merged_array += list1[x:] + list2[y:]
    return merged_array

def split_and_merge(array):
    D = len(array) // 2
    list1 = array[:D]
    list2 = array[D:]

    if len(list1) > 1:
        list1 = split_and_merge(list1)
    if len(list2) > 1:
        list2 = split_and_merge(list2)

    return sort_and_merge(list1, list2)

a = (split_and_merge(a))
print(a) # [-2, 3, 3, 4, 5, 7, 8, 12, 355]


