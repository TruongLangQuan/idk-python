def dura(n):
    count = 0
    while n >= 10:
        n = (n // 10) * (n % 10)
        count += 1
    return count

n = int(input("n:="))
print(dura(n))