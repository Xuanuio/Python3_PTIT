class ThiSinh:
    def __init__(self, id, ten, lt, th):
        self.id = 'TS0' + str(id)
        self.ten = ten
        self.lt = lt
        self.th = th

    def tong(self):
        if self.lt > 10:
            self.lt /= 10
        if self.th > 10:
            self.th /= 10
        return (self.lt + self.th) / 2
    
    def __str__(self):
        d, xl= self.tong(), ''
        if d < 5:
            xl = 'TRUOT'
        elif d < 8:
            xl = 'CAN NHAC'
        elif d <= 9.5:
            xl = 'DAT'
        else:
            xl = 'XUAT SAC'
        return f'{self.id} {self.ten} {d:.2f} {xl}'

if __name__ == '__main__':
    a = []
    n = int(input())
    for i in range(n):
        ten = input()
        lt = float(input())
        th = float(input())
        ts = ThiSinh(i + 1, ten, lt, th)
        a.append(ts)
    a.sort(key = lambda x: -x.tong())
    for x in a:
        print(x)