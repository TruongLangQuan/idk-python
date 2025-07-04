class Hocsinh:
    def __init__(self,ten,lop,diemtb):
        self.ten = ten
        self.lop = lop
        self.diemtb = diemtb

    def hienthi(self):
        print(f"Ten:{self.ten}")
        print(f"Lop:{self.lop}")
        print(f"Diem trung binh:{self.diemtb}")

    def xephang(self):
        if self.diemtb >= 8.5:
            return "Gioi"
        elif self.diemtb >= 6.5:
            return "Kha"
        elif self.diemtb >= 5:
            return "Trung BInh"
        else:
            return "Yeu"
        
danhsach = []
soluong = int(input("So luong hoc sinh:"))

for i in range(soluong):
    print(f"Hoc sinh {i+1}")
    ten = str(input("Ten:"))
    lop = str(input("Lop:"))
    Diemtb = float(input("Diem trung binh:"))
    print("#______________________________#")
    thongtin = Hocsinh(ten,lop,Diemtb)
    danhsach.append(thongtin)

print("Thong tin:")
for thongtin in danhsach:
    thongtin.hienthi()
    print(f"Rank:{thongtin.xephang()}")
    print("**********************")