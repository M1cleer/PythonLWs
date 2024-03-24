import queue
# Задача 1
def is_vowel(ch) :
	ch = ch.upper()
	return (ch == 'А' or ch == 'У'or ch == 'О' or ch == 'Ы'or ch == 'И'
		 or ch == 'Э' or ch == 'Я' or ch == 'Ю' or ch == 'Ё' or ch == 'Е')

def count_diff(string) :
	count = 0
	for i in range(len(string)) :
		if (is_vowel(string[i])) : 
			count += 1
		else:
			count -=1
			
	return abs(count)

def sort_by_diff(inp_list):
	return sorted(inp_list, key=lambda s: count_diff(s))

# inp_list1 = [ "аао", "стол","полёт", "семнадцать" ]
# print(sort_by_diff(inp_list))


# Задача 2
def ascii_weight(string):
    total_weight = sum(ord(i) for i in string)
    return total_weight / len(string)

def sqr_dev(first_wt, wt):
    return (wt - first_wt) ** 2

def sort_strings_by_criteria(inp_list): 
    first_wt = ascii_weight(inp_list[0])
    
    sorted_strings = sorted(inp_list, key=lambda x: sqr_dev(first_wt, ascii_weight(x)))
    
    return sorted_strings

# inp_list = ["weight", "ascii", "sorting", "ASCII"]
# sorted_list = sort_strings_by_criteria(inp_list)
# print(sorted_list)


# Задача 3
def m_avg_ascii_oft(string): # Максимальное среднее трёх символов в строке
	l = []
	m_sum = 0
	for i in string:
		l.append(ord(i))
		sum_l = sum(l)
		if sum_l > m_sum:
			m_sum = sum_l
		if len(l) == 3:
			l.pop(0)

	return m_sum / 3


def sort_by_avg_ascii(strings):
	if len(strings) == 0:
		return
	
	first_wt = ascii_weight(strings[0])

	return sorted(strings, key = lambda x: sqr_dev(first_wt, m_avg_ascii_oft(x)))

inp_strings = ["abcd", "ABC", "feg", "AAA", "eee", "Aeee"]
print(sort_by_avg_ascii(inp_strings))