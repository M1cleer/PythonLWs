def shift_right_one(arr):
    if len(arr) < 1:
        return arr
    
    return [arr[-1]] + arr[:-1]

arr = [10, 20, 30, 40, 50]
shifted_arr = shift_right_one(arr)
print(shifted_arr)