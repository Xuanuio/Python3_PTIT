class DanhBa:
    def __init__(self, ten, sdt, ngay):
        self.ten = ten
        self.sdt = sdt
        self.ngay = ngay

    def __str__(self):
        return f'{self.ten}: {self.sdt} {self.ngay}'

if __name__ == '__main__':
    a = []
    with open('SOTAY.txt', 'r') as f:
        for line in f:
            a.append(line.strip())
    i = 0
    ngay = ''
    while i < len(a):
        if a[i][:4] == 'Ngay':
            ngay = a[i][5:]
            i += 1
        ten = a[i]
        sdt = a[i + 1]
        i += 2
        dt = DanhBa(ten, sdt, ngay)
        print(dt)