from math import sqrt, trunc


def prime(n):
    if n <= 1:
        return False
    for i in range(2,trunc(sqrt(n))):
        if n % 2 == 0:
            return False
    return True

n = int(input())
print(prime(n))