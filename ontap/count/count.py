def count(arr:list[int]):
    count = 0
    
    for i in range(len(arr)):
        if arr[i] % 90 == 0:
            count += 1
    return count

with open("count.inp",'r') as f:
    n = f.read()
    arr = list(map(int,n.split()))

with open("count.out",'w') as f:
    f.write(str(count(arr)))