inp_list = []

while True:
    inp = input()
    if inp == "stop":
        break
    inp_list.append(inp)

inp_list = sorted(inp_list, key=len)

print(inp_list)