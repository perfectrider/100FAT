
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        reference = array[0]
        low = [i for i in array[1:] if i <= reference]
        high = [i for i in array[1:] if i > reference]
        return quicksort(low) + [reference] + quicksort(high)

a = [1, 5, -2, 0, 12, 3, 16]

print(quicksort(a))