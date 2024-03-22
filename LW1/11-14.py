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

inp_list = [ "аао", "стол","полёт", "семнадцать" ]

print(sort_by_diff(inp_list))

