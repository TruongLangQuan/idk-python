input = '/home/tlquan/Documents/idk-python/file I/O/input'
output = '/home/tlquan/Documents/idk-python/file I/O/output'

try:
    with open(input,'r') as input_file:
        noidung = input_file.read()
    
    with open(output,'w') as output_file:
        done = output_file.write(noidung)
        print("Done")
except FileNotFoundError:
    print("Not found")
except Exception as e:
    print(f"Error:{e}")