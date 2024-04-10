def count_min_elements(arr):
    if not arr: 
        return 0

    min_val = min(arr)
    count = arr.count(min_val) 
    return count

arr = [1, 2, 3, 4, 5, 1]
print(count_min_elements(arr))