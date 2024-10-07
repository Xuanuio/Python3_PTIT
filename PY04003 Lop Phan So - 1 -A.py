from math import *

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    x = gcd(tu, mau)
    tu, mau = tu // x, mau // x
    print(f'{tu}/{mau}')