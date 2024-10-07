class GiaoVien:
    def __init__(self, id, ten, ma, diem1, diem2):
        self.id = 'GV' + format(id, '02d')
        self.ten = ten
        self.ma = ma
        self.diem1 = diem1
        self.diem2 = diem2
    
    def tinh_diem(self):
        sum = self.diem1 * 2 + self.diem2
        c = int(self.ma[1])
        if c == 1:
            sum += 2
        elif c == 2:
            sum += 1.5
        elif c == 3:
            sum += 1
        return sum
    
    def mon(self):
        if self.ma[0] == 'A':
            return 'TOAN'
        elif self.ma[0] == 'B':
            return 'LY'
        elif self.ma[0] == 'C':
            return 'HOA'
    
    def xep_loai(self):
        if self.tinh_diem() >= 18:
            return 'TRUNG TUYEN'
        return 'LOAI'
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.mon()} {self.tinh_diem():.1f} {self.xep_loai()}'
    
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        gv = GiaoVien(i+1, input(), input(), float(input()), float(input()))
        a.append(gv)
    a.sort(key = lambda x : -x.tinh_diem())
    for x in a:
        print(x)