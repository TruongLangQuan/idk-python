danhsach = [1,2,3,4,5]
n = int(input("Input n:"))

if n in danhsach:
    danhsach.remove(n)
    print(f"List after remove {n}:{danhsach}")
else:
    print(f"Not found {n} in list")