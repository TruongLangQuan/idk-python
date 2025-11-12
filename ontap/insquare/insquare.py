def inq(a,b):
    count = 0

    for i in range(1,b+1):
        if i**2 <= b and i**2 >= a:
            count += 1
    return count

with open("insquare.inp", "r") as f:
    for i in f:
        n = list(map(int, i.split()))
a = n[0]
b = n[1]
with open("insquare.out", "w") as f:
    f.write(str(inq(a,b)))