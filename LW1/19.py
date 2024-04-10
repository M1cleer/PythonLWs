def sort_by_cr(lst):
    new_lst = sorted(lst, key = lambda x: lst.count(x), reverse=True)
    return new_lst

lst = [5,6,2,2,3,3,3,5,5,5]
print(sort_by_cr(lst))