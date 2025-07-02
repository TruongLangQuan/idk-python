mydict = {}

mydict["Name"] = 'TLQuân'
mydict["Age"] = 14
mydict["Waifu"] = "Ellen Joe"
print(f"{mydict}")

delkey = input("Input key:")

if delkey in mydict:
    mydict.pop(delkey)
    print(f"{mydict}")
else:
    print("Not found")    