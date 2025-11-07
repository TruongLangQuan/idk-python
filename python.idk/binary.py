def binary(n):
    for i in range(2**n):
        print(f"{i:0{n}b}")
    print()

n = int(input("Nhap so bit :"))
binary(n)