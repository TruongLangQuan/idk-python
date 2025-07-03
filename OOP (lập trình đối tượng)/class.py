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
        
ten = str(input("Ten:"))
lop = str(input("Lop:"))
Diemtb = float(input("Diem trung binh:"))

thongtin = Hocsinh(ten,lop,Diemtb)

thongtin.hienthi()

print(f"Rank:{thongtin.xephang()}")