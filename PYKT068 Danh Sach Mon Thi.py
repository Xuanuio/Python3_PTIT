class MonHoc:
    def __init__(self, maMH, tenMH, hinhThucThi):
        self.maMH = maMH
        self.tenMH = tenMH
        self.hinhThucThi = hinhThucThi

    def __str__(self):
        return f'{self.maMH} {self.tenMH} {self.hinhThucThi}'
    
if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        a.append(MonHoc(input(), input(), input()))
    a.sort(key = lambda x: x.maMH)
    for x in a:
        print(x)
        