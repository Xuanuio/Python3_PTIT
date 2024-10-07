from math import *

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return 0
    return 1

def ck(n):
    snt, m = 0, n
    while n != 0:
        r = n % 10
        if r == 2 or r == 3 or r == 5 or r == 7:
            snt += 1
        n //= 10
    return 2 * snt > len(str(m))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if ck(n) and nt(len(str(n))):
            print("YES")
        else:
            print("NO")