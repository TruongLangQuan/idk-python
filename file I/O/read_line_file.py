file_path = '/home/tlquan/Documents/idk-python/file I/O/input'

try:
    with open(file_path,'r') as file:
        for line in file:
            print(line,end='')
except FileNotFoundError:
    print("Not found")
except Exception as e:
    print(f"Error:{e}")