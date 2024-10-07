from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def ck(a):
    f, e = int(a[0:3]), int(a[len(a)-3:])
    if nt(f) and nt(e):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        ck(a)