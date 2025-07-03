myset1 = {'TLQuân', 'Trương Làng Quân','truonglangquan'}
print(f"{myset1}")

remove_set = input("Input:")

myset1.remove(remove_set)
myset1.discard(remove_set)

print(f"Remove:{myset1}")
print(f"Discard:{myset1}")