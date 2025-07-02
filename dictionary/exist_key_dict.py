mydict = {}

mydict["Name"] = 'TLQuân'
mydict["Age"] = 14
mydict["Waifu"] = "Ellen Joe"
print(f"{mydict}")

checkkey = input("Input key:")

if checkkey in mydict:
    print("Found")
else:
    print("Not found")    