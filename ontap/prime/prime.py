def prime(n:int):
    if n <= 1:
        return False
    else: 
        for i in range(2,n ** 0.5):
            if i % 2 == 0:
                return False
            else:
                return True
    return False

def matma(text):
    count = 0
    
    for c in text:
        if c.isdigit():
            if prime(c):
                count += c
    return count

with open("prime.inp",'r') as f:
    text = f.read()
    
with open("prime.out",'w') as f:
    f.write(str(matma(text)))