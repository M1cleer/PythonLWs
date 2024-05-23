def to_int_list(str):
    return set([int(i) for i in str.split()])

n = int(input())
prob_lst = set(range(1, n +1))

while True:
    guess = input()
    if guess == "HELP":
        break
    try:
        guess_lst = to_int_list(guess)
    except:
        continue
    a = input()
    if a == "YES":
        prob_lst &= guess_lst
    else:
        prob_lst -= guess_lst

print(*prob_lst)


# Ввод
# 10
# 2 4 5 6 7
# YES
# 1 3 5 6 7 
# NO
# HELP