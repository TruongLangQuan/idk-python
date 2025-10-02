def xe(n):
    for xe3cho in range(n // 3+1):
        xeconlai = n - xe3cho * 3

        if xeconlai % 2 == 0:
            xe2cho = xeconlai // 2
            return xe2cho,xe3cho
    return None

n = int(input("n:="))

result = xe(n)
if result:
    print(result[0],result[1])
else:
    exit