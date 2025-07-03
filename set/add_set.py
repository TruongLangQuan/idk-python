myset1 = {'TLQuân', 'Trương Làng Quân','truonglangquan'}
print(f"{myset1}")

myset2 = set(['Ellen Joe', 'Lmaoman69','Thi_idk'])
print(f"{myset2}")

new_set = input("Input:")

myset1.update([new_set])
myset2.add(new_set)

print(f"Update:{myset1}")
print(f"Add:{myset2}")