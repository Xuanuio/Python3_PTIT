from math import *

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    x = a * d + b * c
    y = b * d
    z = gcd(x, y)
    x //= z
    y //= z
    print(f'{x}/{y}')