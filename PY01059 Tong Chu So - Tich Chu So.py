from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def ck(a):
    l, c, ok = 1, int(a[0]), 0
    for i in range(1, len(a)):
        res = int(a[i])
        if i % 2 == 0:
            c += res
        else:
            if res != 0:
                ok = 1
                l *= res
    print(c, end = ' ')
    if ok:
        print(l)
    else:
        print(0)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        ck(a)