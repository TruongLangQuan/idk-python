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
    
    def updatediem(self,newdiem):
        self.diemtb = newdiem
        print(f"Diem moi:{self.diemtb}")

    def hi(self):
        print(f"Hi,toi la {self.ten} tu lop {self.lop}")

ten = str(input("Ten:"))
lop = str(input("Lop:"))
Diemtb = float(input("Diem trung binh:"))

if Diemtb > 10:
    print("Fuck you,Nigger")
    exit()
    
thongtin = Hocsinh(ten,lop,Diemtb)

thongtin.hienthi()

print(f"Rank:{thongtin.xephang()}")

diemmoi = int(input("Diem moi:"))
thongtin.updatediem(diemmoi)

thongtin.hi()