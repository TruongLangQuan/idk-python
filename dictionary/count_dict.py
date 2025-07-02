mydict = {}

mydict["Name"] = 'TLQuân'
mydict["Age"] = 14
mydict["Waifu"] = "Ellen Joe"
print(f"{mydict}")

count1 = len(mydict)
print(f"Method 1:{count1}")

count2 = len(mydict.items())
print(f"Method 2:{count2}")

count3 = 0
for _ in mydict:
    count3 += 1
print(f"Method 3:{count3}")