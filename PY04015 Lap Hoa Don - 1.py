class HoaDon:
    def __init__(self, id, ten, cu, moi):
        self.id = 'KH' + format(id, '02d')
        self.ten = ten
        self.cu = cu
        self.moi = moi

    def get_ma(self):
        return self.id

    def tinh_tien(self):
        slg = self.moi - self.cu
        if slg <= 0:
            return 0
        elif slg <= 50:
            return slg * 100 * 1.02
        elif slg <= 100:
            return (50 * 100 + (slg - 50) * 150) * 1.03
        else:
            return (50 * 100 + 50 * 150 + (slg - 100) * 200) * 1.05
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.tinh_tien():.0f}'
    
if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(n):
        ten = input()
        cu, moi = int(input()), int(input())
        hd = HoaDon(i + 1, ten, cu, moi)
        a.append(hd)
    a.sort(key=lambda x: (-x.tinh_tien(), x.get_ma()))
    for x in a:
        print(x)