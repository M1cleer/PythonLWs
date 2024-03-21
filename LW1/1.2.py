def rus_chars(str):
    res = 0
    uni_list = list(range(1040, 1104)) + [1025, 1105]

    for i in str:
        if ord(i) in uni_list:
            res += 1
    
    return res

str = "Аабвг Abcde Ёёя ☻ ♦"
print(rus_chars(str))
