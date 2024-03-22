import re

def find_dates(text):
    pattern = r'\b(\d{1,2})\.(\d{1,2})\.(\d{4})\b'
    matches = re.findall(pattern, text)
    return matches

text = " 29.03.2024 15 шоколадок 21.05.2001."
dates = find_dates(text)
for date in dates:
    print("{}.{}.{}".format(date[0], date[1], date[2]))

