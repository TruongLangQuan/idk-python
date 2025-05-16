import math
from math import sqrt
from math import trunc
def prime(n):
    if n <= 1:
        return False
    for i in range(2, trunc(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("n="))
if prime(n):
    print(f"{n}" is prime) 
else:
    print(f"{n}" is not prime)      