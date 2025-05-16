tong = 0
count = 0
letter = ''

string = str(input("Input string:"))

for i in range(len(string)):
    if string[i].isdigit():
        tong += ord(string[i]) - ord('0')
        count += 1
    
    if string[i].isalpha() or string[i].isspace():
        letter = letter + string[i]

print("tong:=",tong)
print("count:=",count)
print("letter:=",letter)