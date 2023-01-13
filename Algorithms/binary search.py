
a = [5, 3, 12, 355, 356, 7, 8, 4]
a.sort()

def binary_search(data, search_item):
    start = 0
    finish = len(data) - 1

    while start <= finish:
        middle = (start + finish) // 2
        guess = data[middle]
        if guess == search_item:
            return middle + 1
        if guess > search_item:
            finish = middle - 1
        else:
            start = middle + 1

    return 'el is not in array'

print(binary_search(a, 3))
