import re

def find_min_rat_num(input_string):
    pattern = r'[-+]?\d*\.?\d+'
    numbers = re.findall(pattern, input_string)
    
    float_numbers = []
    
    for number in numbers:
        float_numbers.append(float(number))
    
    if len(float_numbers) == 0:
        return None  
    
    min_number = min(float_numbers)
    
    return min_number

input_str = "в строке присутствуют числа: 25325423, 3.15 и -2.71"
min_rational = find_min_rat_num(input_str)

print(min_rational) 
