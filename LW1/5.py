import re

def find_dates(str):
    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    months_reg = "|".join(months)

    pattern = r'\b(\d{1,2})\ (' + months_reg + r')\ (\d{4})\b'

    matches = re.findall(pattern, str)
    return matches

text = "1 июня 2024 года начнется лето в 2024 году. 20 ноября 2024 года будет в ноябре"
dates = find_dates(text)

for date in dates:
    print("{} {} {}".format(date[0], date[1], date[2]))