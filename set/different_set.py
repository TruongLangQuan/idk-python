#Tìm phần bù trong 2 set(Tìm ra các phần tử trong set 1 có mà set 2 ko)
myset1 = {'Thi_idk','TLQuân', 'Trưởng Làng Quân','truonglangquan'}
print(f"{myset1}")

myset2 = set(['Ellen Joe', 'Lmaoman69','Thi_idk'])
print(f"{myset2}")

different_set = myset1 - myset2

print(f"Phần bù trong set:{different_set}")