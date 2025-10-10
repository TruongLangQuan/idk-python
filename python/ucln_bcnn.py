def ucln(a,b):
    while b != 0:
        a ,b = b , a % b
    return a

def bcnn(a,b):
    result = (a*b) // ucln(a,b)
    return result

a = int(input("a:="))
b = int(input("b:="))

print(ucln(a,b))
print(bcnn(a,b))