file_path = '/home/tlquan/Documents/idk-python/file I/O/output'
vanban = str(input("Nhap noi dung:"))
try:
    with open(file_path,'a') as file:
        file.write(vanban)
        print(f"Noi dung dc ghi vao:{file_path}")
except Exception as e:
    print(f"Error:{e}")