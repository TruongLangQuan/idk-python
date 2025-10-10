import subprocess
import os

# Bước 1: Chọn file .py để test
py_files = [f for f in os.listdir() if f.endswith('.py') and f != 'bot_tatca.py']
if not py_files:
    print("❌ Không tìm thấy file Python nào.")
    exit()

print("📂 Danh sách file:")
for i, f in enumerate(py_files, 1):
    print(f"{i}. {f}")

try:
    file_idx = int(input("👉 Nhập số tương ứng file cần test: "))
    if not (1 <= file_idx <= len(py_files)):
        raise ValueError
except:
    print("❌ Số không hợp lệ.")
    exit()

filename = py_files[file_idx - 1]

# Bước 2: Chọn kiểu input
os.system("clear")
print("🔢 Chọn kiểu input:")
print("1. Tự động test từ 1 đến 2025")
print("2. Một số nguyên")
print("3. Nhiều số nguyên")
print("4. Một chuỗi")
print("5. Nhiều chuỗi")
input_type = input("👉 Nhập kiểu (1/2/3/4/5): ").strip()

os.system("clear")

# ✅ Bước 3: Tự động test từ 1 đến 2025
if input_type == "1":
    print(f"🚀 Đang test file: {filename}\n")
    for i in range(1, 2026):
        result = subprocess.run(
            ['python', filename],
            input=str(i),
            text=True,
            capture_output=True
        )
        print(f"🧪 Test input: {i}")
        if result.stdout.strip():
            print("📤 Output:", result.stdout.strip())
        else:
            print("⚠️ Không có output (stdout rỗng)")
            if result.stderr.strip():
                print("🧨 stderr:", result.stderr.strip())
        print("-" * 40)
    print("\n✅ Đã hoàn tất test từ 1 đến 2025")
    exit()

# Các kiểu input bình thường
user_inputs = []

if input_type == "2":
    value = input("🔸 Nhập số nguyên: ")
    user_inputs = [value]

elif input_type == "3":
    n = int(input("🔸 Nhập số dòng chứa số nguyên: "))
    for i in range(n):
        user_inputs.append(input(f"  Dòng {i+1}: "))

elif input_type == "4":
    value = input("🔸 Nhập chuỗi: ")
    user_inputs = [value]

elif input_type == "5":
    n = int(input("🔸 Nhập số dòng chuỗi: "))
    for i in range(n):
        user_inputs.append(input(f"  Dòng {i+1}: "))

else:
    print("❌ Kiểu input không hợp lệ.")
    exit()

# Bước 4: Chạy file với input tự nhập
full_input = "\n".join(user_inputs)
os.system("clear")

print(f"🚀 Đang test file: {filename}\n")
print("===== INPUT =====")
print(full_input)
print("=================")

result = subprocess.run(
    ['python', filename],
    input=full_input,
    text=True,
    capture_output=True
)

print("\n===== OUTPUT =====")
print(result.stdout.strip())
print("==================")