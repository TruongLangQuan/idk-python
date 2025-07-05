file_path = '/home/tlquan/Documents/idk-python/file I/O/input'
try:
    with open(file_path,'r') as file:
        noidung = file.read()
        print(f"Noi dung:")
        print(noidung)
except FileNotFoundError:
    print("Not found")
except Exception as e:
    print(f"Error:{e}")