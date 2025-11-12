def diem(arr):
    result = 0
    temp = 0
    
    for i in arr:
        for val in i:
            temp += val
            if temp >= 200:
                result = temp
                return result
    return result

arr = []
with open("pumpks.inp", "r") as f:
    for i in f:
        n = list(map(int, i.split()))
        arr.append(n)

with open("pumpks.out",'w') as f:
    f.write(str(diem(arr)))
    