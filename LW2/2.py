n = int(input()) 
dct = {}

for _ in range(n): # Ввод стран и городов
    inp = input()
    inp_lst = inp.split()
    for i in inp_lst[1:]:
        dct[i] = inp_lst[0]

n = int(input())
inp_lst = []

for _ in range(n): # Проверка городов
    inp = input()
    inp_lst.append(inp)

for i in inp_lst:
    print(dct.get(i))