class ThiSinh:
    def __init__(self, ten, dv, end):
        self.ten = ten
        self.dv = dv
        self.end = end
    
    def id(self):
        dau = self.dv.split()
        cuoi = self.ten.split()
        ma = ''
        for x in dau:
            ma += x[0]
        for x in cuoi:
            ma += x[0]
        return ma.upper()
    
    def van_toc(self):
        e = self.end.split(':')
        t = 0
        t = int(e[0]) - 6 
        t += int(e[1]) / 60
        v = 120 / t
        return v
    
    def __str__(self):
        return f'{self.id()} {self.ten} {self.dv} {self.van_toc():.0f} Km/h'

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        ts = ThiSinh(input(), input(), input())
        a.append(ts)
    a.sort(key = lambda x: x.van_toc(), reverse = True)
    for x in a:
        print(x)