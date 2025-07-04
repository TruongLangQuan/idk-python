try:
    mylist = [1,2,3,4,5]
    element = mylist[6]
except IndexError:
    element = "Bruh"

print(f"{element}")