from math import *

nt = [1] * 1000007

def seive():
    nt[0] = nt[1] = 0
    for i in range(2, 1000007):
        if nt[i]:
            for j in range(i*i, 1000007, i):
                nt[j] = 0

def ck():
    for i in range(2, 1000001):
        if nt[i] and nt[i+6] and (nt[i+2] or nt[i+4]):
            nt[i] = 1
        else:
            nt[i] = 0

if __name__ == '__main__':
    seive()
    ck()
    t = int(input())
    for _ in range(t):
        n = int(input())
        sum = 0
        for i in range(2, n+1):
            if nt[i] and i + 6 <= n:
                sum += 1
        print(sum)