def giaithua(n):
    result = 1
    if n == 0:
        return result
    else:
        for i in range(1,n+1):
            result = result*i
        return result

n = int(input("Input n:"))
print("Result:",(giaithua(n)))