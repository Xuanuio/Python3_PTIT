class HoaDon:
    def __init__(self, id, ten, slg, dongia, chietkhau):
        self.id = id
        self.ten = ten
        self.slg = slg
        self.dongia = dongia
        self.chietkhau = chietkhau

    def thanhtien(self):
        return self.slg * self.dongia - self.chietkhau
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.slg} {self.dongia} {self.chietkhau} {self.thanhtien()}'
    
if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(HoaDon(input(), input(), int(input()), int(input()), int(input())))
    a.sort(key=lambda x: -x.thanhtien())
    for x in a:
        print(x)