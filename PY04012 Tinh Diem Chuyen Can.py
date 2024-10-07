class SinhVien:
    def __init__(self, id, ten, lop, cc):
        self.id = id
        self.ten = ten
        self.lop = lop
        self.cc = cc

    def ghi_chu(self):
        ck, d = self.cc, 10
        for x in ck:
            if x == 'm':
                d -= 1
            elif x == 'v':
                d -= 2
        if d <= 0:
            return '0 KDDK'
        return str(d)

    def __str__(self):
        return f'{self.id} {self.ten} {self.lop} {self.ghi_chu()}'
    
if __name__ == '__main__':
    a, c = [], []
    n = int(input())
    for _ in range(n):
        b = []
        for _ in range(3):
            b.append(input())
        a.append(b)
    for _ in range(n):
       c.append(input())
    for i in range(n):
        for j in range(n):
            if a[i][0] == c[j][:10]:
                sv = SinhVien(a[i][0], a[i][1], a[i][2], c[j][11:])
                print(sv)
                break 