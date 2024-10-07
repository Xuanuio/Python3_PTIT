from functools import cmp_to_key
from datetime import datetime

class LichThiHocKy:
    def __init__(self, id, maMH, tenMH, ngay, gio, nhom):
        self.id = 'T' + format(id, '03d')
        self.maMH = maMH
        self.tenMH = tenMH
        self.ngay = ngay
        self.gio = gio
        self.nhom = nhom

    def get_id(self):
        return self.id
    
    def get_maMH(self):
        return self.maMH

    def get_ngay(self):
        return self.ngay
    
    def get_gio(self):
        return self.gio
    
    def get_nhom(self):
        return self.nhom

    def __str__(self):
        return f'{self.id} {self.maMH} {self.tenMH} {self.ngay} {self.gio} {self.nhom}'
    
def cmp(a, b):
    n1 = a.get_ngay().split('/')
    g1 = a.get_gio().split(':')
    n2 = b.get_ngay().split('/')
    g2 = b.get_gio().split(':')
    d1 = datetime(int(n1[2]), int(n1[1]), int(n1[0]), int(g1[0]), int(g1[1]))
    d2 = datetime(int(n2[2]), int(n2[1]), int(n2[0]), int(g2[0]), int(g2[1]))
    if d1 == d2:
        if a.get_nhom() == b.get_nhom():
            return a.get_maMH() < b.get_maMH()
        return a.get_nhom() < b.get_nhom()
    elif d1 < d2:
        return -1
    else:
        return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b, c = [], [], []
    for _ in range(n):
        b.append(input())
        c.append(input())
    for i in range(m):
        z, t, u, v = map(str, input().split())
        for j in range(n):
            if z == b[j]:
                f = LichThiHocKy(i+1, z, c[j], t, u, v)
                a.append(f)
                break
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        print(x)