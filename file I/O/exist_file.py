import os
file_path = '/home/tlquan/Documents/idk-python/file I/O/input'

if os.path.isfile(file_path):
    print("Found")
else:
    print("Not Found")