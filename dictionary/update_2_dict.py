mydict = {}

mydict["Name"] = 'TLQuân'
mydict["Age"] = 14
mydict["Waifu"] = "Ellen Joe"
print(f"{mydict}")

mydict2 = {
    "Acc":'Thi_idk',
    "Tiktok":'truonglangquan',
    "YT":'truonglangquan69'
}
print(f"{mydict2}")

mydict3 = mydict.copy()
mydict3.update(mydict2)
print(f"Method 1:{mydict3}")

mydict4 = {**mydict,**mydict2}
print(f"Method 2:{mydict4}")