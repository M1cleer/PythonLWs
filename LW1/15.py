def shift_right(arr):
    if len(arr) < 2:
        return arr
    
    return arr[-2:] + arr[:-2]

arr = [1, 2, 3, 4, 5]
print(shift_right(arr))