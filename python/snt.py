import math
from math import trunc
from math import sqrt

def prime(n):
    if n <= 1:
        return False
    for i in range(1,trunc(sqrt(n))):
        if n % 2 == 0:
            return False
    return True

n = input("n:=")
if n == 'hau':
    print("haugay")
else:
    print(prime(n))