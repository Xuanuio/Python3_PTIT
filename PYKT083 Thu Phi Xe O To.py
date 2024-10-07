class Xe:
    def __init__(self, bienso, loaixe, soghe, huong, ngay):
        self.bienso = bienso
        self.loaixe = loaixe
        self.soghe = soghe
        self.huong = huong
        self.ngay = ngay
    
    def tinh_tien(self):
        if self.huong == 'OUT':
            return 0
        else:
            if self.soghe == 2:
                return 20000
            elif self.soghe == 5:
                return 10000
            elif self.soghe == 7:
                return 15000
            elif self.soghe == 29:
                return 50000
            else:
                return 70000
        
if __name__ == '__main__':
    d = dict([])
    t = int(input())
    for _ in range(t):
        bienso, loaixe, soghe, huong, ngay = input().split()
        x = Xe(bienso, loaixe, int(soghe), huong, ngay)
        if x.ngay not in d:
            d[x.ngay] = x.tinh_tien()
        else:
            d[x.ngay] += x.tinh_tien()
    for key, value in sorted(d.items()):
        print(f'{key}: {value}')