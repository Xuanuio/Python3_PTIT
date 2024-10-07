def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def tong(self, ps):
        tu = self.tu * ps.mau + self.mau * ps.tu
        mau = self.mau * ps.mau
        x = gcd(tu, mau)
        tu //= x
        mau //= x
        return f'{tu}/{mau}'
    
if __name__ == '__main__':
    tu1, mau1, tu2, mau2 = map(int, input().split())
    ps1 = PhanSo(tu1, mau1)
    ps2 = PhanSo(tu2, mau2)
    print(ps1.tong(ps2))