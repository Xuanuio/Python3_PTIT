from math import *

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ok = 1
        for i in range(2, n):
            if gcd(i, n) == 1:
                ok += 1
        if nt(ok):
            print("YES")
        else:
            print("NO")