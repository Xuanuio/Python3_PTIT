def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        x = gcd(self.tu, self.mau)
        self.tu //= x
        self.mau //= x

    def __str__(self):
        return f'{self.tu}/{self.mau}'
    
if __name__ == '__main__':
    tu, mau = map(int, input().split())
    ps = PhanSo(tu, mau)
    ps.rutgon()
    print(ps)