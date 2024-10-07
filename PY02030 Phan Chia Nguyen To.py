from math import *

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for x in a:
        if x not in b:
            b.append(x)
    l, r, m, ok = 0, sum(b), len(b), 1
    for i in range(m):
        l += b[i]
        r -= b[i]
        if nt(l) and nt(r):
            print(i)
            ok = 0
            break
    if ok:
        print('NOT FOUND')