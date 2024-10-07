class NhanVien:
    def __init__(self, id, ten, phong_ban, luong_cb, ngay_cong):
        self.id = id
        self.ten = ten
        self.phong_ban = phong_ban
        self.luong_cb = luong_cb
        self.ngay_cong = ngay_cong

    def he_so(self):
        s = self.id[0]
        year = int(self.id[1:3])
        if s == 'A':
            if year <= 3:
                return 10
            elif year <= 8:
                return 12
            elif year <= 15:
                return 14
            else:
                return 20
        elif s == 'B':
            if year <= 3:
                return 10
            elif year <= 8:
                return 11
            elif year <= 15:
                return 13
            else:
                return 16
        elif s == 'C':
            if year <= 3:
                return 9
            elif year <= 8:
                return 10
            elif year <= 15:
                return 12
            else:
                return 14
        else:
            if year <= 3:
                return 8
            elif year <= 8:
                return 9
            elif year <= 15:
                return 11
            else:
                return 13
    
    def tinh_luong(self):
        return self.luong_cb * self.he_so() * self.ngay_cong * 1000
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.phong_ban} {self.tinh_luong()}'
    
if __name__ == '__main__':
    n = int(input())
    a, b = [], []
    for _ in range(n):
        l = []
        s = input()
        l.append(s[:2])
        l.append(s[3:])
        b.append(l)
    t = int(input())
    for _ in range(t):
        x = input()
        for i in range(n):
            if x[-2:] == b[i][0]:
                nv = NhanVien(x, input(), b[i][1], int(input()), int(input()))
                print(nv)
                break