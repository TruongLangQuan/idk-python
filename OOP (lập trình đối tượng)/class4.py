#Thuộc tính của đối tượng(public và private)
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
        
    @property
    def tuoi(self):
        return self._tuoi
    
    @tuoi.setter
    def tuoi(self,newtuoi):
        if newtuoi > 0:
            self._tuoi = newtuoi
        else:
            print("Nah")
            exit()    
        
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

for i,thongtin in enumerate(danhsach):
    print(f"Hoc sing {i+1}:{thongtin.ten}")
    newtuoi = int(input("Update tuoi:"))
    print("============================")
    thongtin.tuoi = newtuoi

for thongtin in danhsach:
    print("Thong tin:")
    thongtin.hienthi()
    print(f"Rank:{thongtin.xephang()}")
    print("===========================")