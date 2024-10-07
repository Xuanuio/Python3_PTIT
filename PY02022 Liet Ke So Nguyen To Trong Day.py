from math import *

nt = [1] * 1000005

def sieve():
    nt[0] = nt[1] = 0
    for i in range(2, isqrt(1000005)):
        if nt[i]:
            for j in range(i*i, 1000005, i):
                nt[j] = 0

if __name__ == '__main__':
    sieve()
    n = int(input())
    a = list(map(int, input().split()))
    d = dict([])
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in d:
        if nt[x]:
            print(x, d[x])