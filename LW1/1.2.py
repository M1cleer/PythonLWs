def rus_chars(input_str):
    res = 0
    uni_list = list(range(1040, 1104)) + [1025, 1105]

    for i in input_str:
        if ord(i) in uni_list:
            res += 1
    
    return res

input_str = "Аабвг Abcde Ёёя ☻ ♦"
print(rus_chars(input_str))
