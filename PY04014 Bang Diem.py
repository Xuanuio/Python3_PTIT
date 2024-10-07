class HocSinh:
    def __init__(self, id, ten, toan, van, anh, ly, hoa, sinh, su, dia, gdcd, cn):
        self.id = 'HS' + format(id, '02d')
        self.ten = ten
        self.toan = toan
        self.van = van
        self.anh = anh
        self.ly = ly
        self.hoa = hoa
        self.sinh = sinh
        self.su = su
        self.dia = dia
        self.gdcd = gdcd
        self.cn = cn

    def get_ma(self):
        return self.id
    
    def diem_tb(self):
        return (self.toan * 2 + self.van * 2 + self.anh + self.ly + self.hoa + self.sinh + self.su + self.dia + self.gdcd + self.cn + 0.07) / 12
        # + 0.07 --> 0.05 được làm tròn lên 

    def __str__(self):
        xl = ''
        if self.diem_tb() >= 9:
            xl = 'XUAT SAC'
        elif self.diem_tb() >= 8:
            xl = 'GIOI'
        elif self.diem_tb() >= 7:
            xl = 'KHA'
        elif self.diem_tb() >= 5:
            xl = 'TB'
        else:
            xl = 'YEU'
        return f'{self.id} {self.ten} {self.diem_tb():.1f} {xl}'
    
if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(n):
        ten = input()
        toan, van, anh, ly, hoa, sinh, su, dia, gdcd, cn = map(float, input().split())
        hs = HocSinh(i + 1, ten, toan, van, anh, ly, hoa, sinh, su, dia, gdcd, cn)
        a.append(hs)
    a.sort(key = lambda x: (-x.diem_tb(), x.get_ma()))
    for x in a:
        print(x)