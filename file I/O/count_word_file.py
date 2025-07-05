file_path = '/home/tlquan/Documents/idk-python/file I/O/input'
try:
    with open(file_path,'r') as file:
        count = 0
        for line in file:
            word = line.split()
            count += len(word)
        print(f"Count:{count}")    
except FileNotFoundError:
    print("Not found")
except Exception as e:
    print(f"Error:{e}")