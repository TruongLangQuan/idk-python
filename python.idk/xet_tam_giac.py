def inputc():
    a = float(input("Nhap canh 1:"))
    b = float(input("Nhap canh 2:"))
    c = float(input("Nhap canh 3:"))
    return a,b,c

def xet(a,b,c):
    return ((a>0) and (b > 0) and (c > 0) and (a+b > c) and (a+c > b) and (b+c > a))

def loaitamgiac(a,b,c):
    if xet(a,b,c) == True:
        if (a**2) == (c**2) - (b**2):
            return "Tam Giac Vuong"
        if a == b == c:
            return "Tam Giac Deu"
        if (a**2) == (c**2) - (b**2) and (a == b):
            return "Tam Giac Vuong Can"
        if (a == b) or (a == c) or (b == c):
            return "Tam Giac Can"
        if (a != b != c) and (c**2) != (a**2) + (b**2):
            return "Tam Giac Thuong"
        
a,b,c = inputc()

print(loaitamgiac(a,b,c))