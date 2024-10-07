from functools import cmp_to_key
from datetime import datetime

class Phim:
    def __init__(self, id, theloai, ngaykhoichieu, tenphim, sotap):
        self.id = 'P' + format(id, '03d')
        self.theloai = theloai
        self.ngaykhoichieu = ngaykhoichieu
        self.tenphim = tenphim
        self.sotap = sotap

    def ngay(self):
        return self.ngaykhoichieu
    
    def ten(self):
        return self.tenphim
    
    def tap(self):
        return self.sotap
    
    def __str__(self):
        return f'{self.id} {self.theloai} {self.ngaykhoichieu} {self.tenphim} {self.sotap}'

def cmp(a, b):
    if a.ngay() == b.ngay():
        if a.ten() == b.ten():
            return a.tap() - b.tap()
        return a.ten() < b.ten()
    else:
        n1 = a.ngay().split('/')
        n2 = b.ngay().split('/')
        d1 = datetime(int(n1[2]), int(n1[1]), int(n1[0]))
        d2 = datetime(int(n2[2]), int(n2[1]), int(n2[0]))
        if d1 < d2:
            return -1
        elif d1 > d2:
            return 1
            
if __name__ == '__main__':
    n, m = map(int, input().split())
    a, tl = [], []
    for _ in range(n):
        tl.append(input())
    for i in range(m):
        s = input()
        stt = int(s[2:])
        f = Phim(i+1, tl[stt-1], input(), input(), int(input()))
        a.append(f)
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        print(x)