from math import *

global a

def nt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

def snt():
    cnt = 0
    while cnt < 100:
        for i in range(2, 10000):
            if nt(i):
                a.append(i)
                cnt += 1

if __name__ == '__main__':
    a = []
    snt()
    n, x = map(int, input().split())
    print(x, end=' ')
    for i in range(0, n):
        x += a[i]
        print(x, end=' ')