mystring = "hello"

count = {}

for ky_tu in mystring:
    count[ky_tu] = 0
for ky_tu in mystring:    
    if ky_tu in mystring:
        count[ky_tu] += 1

print(count)