class ThiSinh:
    def __init__(self, id, ten, diem, dt, kv):
        self.id = 'TS' + format(id, '02d')
        self.ten = ten
        self.diem = diem
        self.dt = dt
        self.kv = kv

    def tong_diem(self):
        sum = self.diem
        if self.dt != 'Kinh':
            sum += 1.5
        if self.kv == 1:
            sum += 1.5
        if self.kv == 2:
            sum += 1
        return sum
    
    def trang_thai(self):
        if self.tong_diem() >= 20.5:
            return 'Do'
        return 'Truot'
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.tong_diem():.1f} {self.trang_thai()}'
    
if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        ten = input().split()
        name = ' '.join(ten).title()
        diem = float(input())
        dt = input()
        kv = int(input())
        ts = ThiSinh(i+1, name, diem, dt, kv)
        a.append(ts)
    a.sort(key = lambda x: (-x.tong_diem(), x.id))
    for x in a:
        print(x)