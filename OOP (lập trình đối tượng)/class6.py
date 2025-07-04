#Kế thừa từ một lớp cơ bản
class Human:
    def __init__(self,ten,tuoi):
        self.ten = ten
        self.tuoi = tuoi

    def hienthi(self):
        print(f"Ten:{self.ten}")
        print(f"Tuoi:{self.tuoi}")

class Hocsinh(Human):
    def __init__(self, ten,tuoi,lop,diemtb):
        super().__init__(ten, tuoi)
        self.lop = lop
        self.diemtb = diemtb

    def thongtin(self):
        super().hienthi()
        print(f"Lop:{self.lop}")
        print(f"Diem trung binh:{self.diemtb}")

    def xephang(self):
        if self.diemtb >= 8.5:
            return "Gioi"
        elif self.diemtb >= 6.5:
            return "Kha"
        elif self.diemtb >= 5:
            return "Trung Binh"
        else:
            return "You cooked bro"

danhsach = []
soluong = int(input("So luong hoc sinh:"))

for i in range(soluong):
    print(f"Hoc sinh {i+1}")
    ten = str(input("Ten:"))
    tuoi = int(input("Tuoi:"))
    lop = str(input("Lop:"))
    diemtb = float(input("Diem trung binh:"))
    print("|===================================|")
    thongtin = Hocsinh(ten,tuoi,lop,diemtb)
    danhsach.append(thongtin)

for thongtin in danhsach:
    thongtin.thongtin()
    print(f"Rank:{thongtin.xephang()}")
    print("|===================================|")