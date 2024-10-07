from math import *

def nt(x):
    if x < 2:
        return 0
    for i in range(2, isqrt(x) + 1):
        if x % i == 0:
            return 0
    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if nt(a[i][j]):
                a[i][j] = 1
            else:
                a[i][j] = 0
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()