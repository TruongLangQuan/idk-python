import os
file_path = '/home/tlquan/Documents/idk-python/file I/O/test'

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File remove")
else:
    print("Not found")