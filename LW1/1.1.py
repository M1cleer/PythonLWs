def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def prime_sum(number):
    sum = 1
    for i in range(2, number+1):
        if is_prime(i) and number % i == 0:
            sum += i

    return sum

print(prime_sum(17))  # 1 + 3 = 4