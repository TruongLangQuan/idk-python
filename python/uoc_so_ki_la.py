def weird(a,b):
    count = 0
    for i in range(a,b+1):
        for j in range(2,b+1):
            if (i // j == i % j):
                count += 1
    return count

a = int(input("a:="))
b = int(input("b:="))

print(weird(a,b))