#Sẽ in ra giá trị của key, Vd: key:age sẽ ra value:14
mydict = {}

mydict["Name"] = 'TLQuân'
mydict["Age"] = 14
mydict["Waifu"] = "Ellen Joe"

key = input("Input key:")
if key in mydict:
    result = mydict[key]
    print(f"{result}")
else:
    print(f"Not found {key}")    