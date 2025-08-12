array = [4, 3, 2, 1, 5, 6, 7, 9, 8]

def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


print(linear_search(array, 5))
print(linear_search(array, 10))