class Hocsinh:
    def __init__(self,ten,lop,diemtb):
        self.ten = ten
        self.lop = lop
        self.diemtb = diemtb
    
    def hienthi(self):
        print(f"Ten Hoc Sinh:{self.ten}")
        print(f"Lop:{self.lop}")
        print(f"Diem trung binh:{self.diemtb}")

    def xephang(self):
        if self.diemtb <= 5:
            return "Ngu -1"
        if self.diemtb >= 6.5:
            return "Kha"
        if self.diemtb >= 8:
            return "Gioi"
        if self.diemtb >= 9:
            return "Vip"

ten = str(input("Ten:"))
lop = str(input("Lop:"))
diemtb = float(input("Diem trung binh:"))

thongtin = Hocsinh(ten,lop,diemtb)
thongtin.hienthi()

print(thongtin.xephang())