mydict = {}

mydict["Name"] = 'TLQuân'
mydict["Age"] = 14
mydict["Waifu"] = "Ellen Joe"

print(f"{mydict}")
new_key = input("Input key:")
new_value = input("Input value:")

mydict[new_key] = new_value

print(f"{mydict}")