file_path = '/home/tlquan/Documents/idk-python/file I/O/input'
try:
    with open(file_path,'r') as file:
        noidung = file.read()
        letter = ''.join(c for c in noidung if c not in(' ','\n','\t'))
        count = len(letter)
        print(f"Count:{count}")    
except FileNotFoundError:
    print("Not found")
except Exception as e:
    print(f"Error:{e}")