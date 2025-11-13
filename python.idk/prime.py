import math
from math import sqrt
from math import trunc

def prime(n):
    if n <= 1:
        return False
    for i in range(1,trunc(sqrt(n))):
        if n % 2 == 0:
            return False
    return True

n = int(input("n:="))
print(prime(n))