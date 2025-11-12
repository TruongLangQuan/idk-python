def diem(arr):
    result = 0
    
    for i in arr:
        result += int(i)
        if result >= 200:
            break
    return result

arr = []
with open("pumpks.inp", "r") as f:
    for i in f:
        n = list(map(int, i.split()))
    arr.append(n)

with open("pumpks.out",'w') as f:
    f.write(diem(arr))
    