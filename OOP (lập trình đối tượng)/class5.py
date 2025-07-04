class Hocsinh:
    def __init__(self,ten,tuoi,lop,diemtb):
        self.ten = ten
        self.tuoi = tuoi
        self.lop = lop
        self.diemtb = diemtb

    def hienthi(self):
        print(f"Ten:{self.ten}")
        print(f"Tuoi:{self.tuoi}")
        print(f"Lop:{self.lop}")
        self.__xep_hang()

    def xephang(self):
        if self.diemtb >= 8.5:
            return "Gioi"
        elif self.diemtb >= 6.5:
            return "Kha"
        elif self.diemtb >= 5:
            return "Trung BInh"
        else:
            return "Yeu"

    def __xep_hang(self):
        rank = self.xephang()
        print(f"Rank:{rank}")

danhsach = []
soluong = int(input("So luong hoc sinh:"))

for i in range(soluong):
    print(f"Hoc sinh {i+1}")
    ten = str(input("Ten:"))
    tuoi = int(input("Tuoi:"))
    lop = str(input("Lop:"))
    Diemtb = float(input("Diem trung binh:"))
    if Diemtb > 10:
        print("Bruh")
        exit()
    print("#______________________________#")
    thongtin = Hocsinh(ten,tuoi,lop,Diemtb)
    danhsach.append(thongtin)

for thongtin in danhsach:
    print("Thong tin:")
    thongtin.hienthi()
    print(f"Rank:{thongtin.xephang()}")
    print("===========================")        