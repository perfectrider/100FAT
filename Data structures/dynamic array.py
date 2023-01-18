
# The list data type in Python is a dynamic array

lst = [1, 2, 3, 4]
lst2 = [True, 'Истина', 1, 1.25]

lst.append(5)        # O(1)
lst.insert(0, 1.2)   # O(n)
print(f'{lst}, length={len(lst)}')

elem3 = lst[0]       # O(1)

list3 = lst + lst2   # O(n + m) где n и m длинна lst и lst1 соответственно

lst = list3[0:3]     # O(n)