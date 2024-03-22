import re 

def gst_sequence(input_str):

    pattern = r'\d+'

    matches = re.findall(pattern, input_str)
    return max(matches, key = len)


input_str = "abcde 17 1 7, hjf 091"
print(gst_sequence(input_str))
