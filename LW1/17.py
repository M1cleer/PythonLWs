def find_evens(arr):
    counter = 0
    for i in arr:
        if type(i) is int and not (i & 1):
            counter += 1

    return counter

arr = [1, 2, 3, 4, 5]
print(find_evens(arr))