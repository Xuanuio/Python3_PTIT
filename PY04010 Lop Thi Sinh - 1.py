class ThiSinh:
    def __init__(self, ten, ns, toan, ly, hoa):
        self.ten = ten
        self.ns = ns
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
    
    def tong(self):
        return self.toan + self.ly + self.hoa
    
    def __str__(self):
        return f'{self.ten} {self.ns} {self.tong():.1f}'
    
if __name__ == '__main__':
    ten = input()
    ns = input()
    toan = float(input())
    ly = float(input())
    hoa = float(input())
    ts = ThiSinh(ten, ns, toan, ly, hoa)
    print(ts)