class KhachHang:
    def __init__(self, id, ten, loai, dau, cuoi):
        self.id = 'KH' + format(id, '02d')
        self.ten = ten
        self.loai = loai
        self.dau = dau
        self.cuoi = cuoi
    
    def trongDM(self):
        if self.loai == 'A':
            return min(45000, (self.cuoi - self.dau) * 450)
        elif self.loai == 'B':
            return min(500 * 450, (self.cuoi - self.dau) * 450)
        else:
            return min(90000, (self.cuoi - self.dau) * 450)
        
    def ngoaiDM(self):
        if self.loai == 'A':
            return max(0, ((self.cuoi - self.dau) - 100) * 1000)
        elif self.loai == 'B':
            return max(0, ((self.cuoi - self.dau) - 500) * 1000)
        else:
            return max(0, ((self.cuoi - self.dau) - 200) * 1000)
        
    def VAT(self):
        return self.ngoaiDM() // 20
    
    def tongTien(self):
        return self.trongDM() + self.ngoaiDM() + self.VAT()
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.trongDM()} {self.ngoaiDM()} {self.VAT()} {self.tongTien()}'
    
if __name__ == '__main__':
    n = int(input())
    a = []
    for j in range(n):
        s = input().split()
        ten = ' '.join(s).title()
        b = list(map(str, input().split()))
        u, i, o = b[0], int(b[1]), int(b[2])
        kh = KhachHang(j+1, ten, u, i, o)
        a.append(kh)
    a.sort(key=lambda x: -x.tongTien())
    for kh in a:
        print(kh)