import re

def max_float_in_str(input_str):
    pattern = r'[-]?[0-9]*\.[0-9]+'
    matches = [float(i) for i in re.findall(pattern, input_str)]
    return max(matches) if matches else float('-inf')

text = "abc 13.213, 10, 105, .1, abcd150.32 102.12"

print(max_float_in_str(text))
