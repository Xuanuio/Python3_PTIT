from math import ceil

class SinhVien:
    def __init__(self, id, ten, diem1, diem2, diem3):
        self.id = 'SV' + format(id, '02d')
        self.ten = ten
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3

    def diem_trung_binh(self):
        sum = (self.diem1 * 3 + self.diem2 * 3 + self.diem3 * 2) / 8
        return ceil(sum * 100) / 100
        # return (self.diem1 * 3 + self.diem2 * 3 + self.diem3 * 2) / 8 + 0.0045
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.diem_trung_binh():.2f}'
    
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ten = input().split()
        name = ' '.join(ten).title()
        sv = SinhVien(i+1, name, float(input()), float(input()), float(input()))
        a.append(sv)
    a.sort(key = lambda x: (-x.diem_trung_binh(), x.id))
    cnt = 1
    print(a[0] , 1)
    for i in range(1, n):
        if a[i].diem_trung_binh() == a[i-1].diem_trung_binh():
            print(a[i], cnt)
        else:
            print(a[i], i+1)
            cnt = i+1