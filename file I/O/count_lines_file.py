file_path = '/home/tlquan/Documents/idk-python/file I/O/input'
try:
    with open(file_path,'r') as file:
        count = sum(1 for line in file)
        print(f"Count:{count}")
except FileNotFoundError:
    print("Not found")
except Exception as e:
    print(f"Error:{e}")