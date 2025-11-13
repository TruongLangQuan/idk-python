from math import sqrt
from math import trunc

def prime(n):
    if n <= 1:
        return False
    for i in range(1,trunc(sqrt(n))):
        if n % 2 == 0:
            return False
    return True

def matma(text):
    count = 0
    
    for c in text:
        if c.isdigit():
            if prime(int(c)):
                count += int(c)
    return count

with open("prime.inp",'r') as f:
    text = f.read()
    
with open("prime.out",'w') as f:
    f.write(str(matma(text)))