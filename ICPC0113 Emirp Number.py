from math import *

nt = [1] * 1000001
cnt = [0] * 1000001

def seive():
    nt[0] = nt[1] = 0
    for i in range(2, 1000001):
        if nt[i]:
            for j in range(i*i, 1000001, i):
                nt[j] = 0

def nguoc(n):
    s = str(n)
    s = s[::-1]
    return int(s)

def ck():
    for i in range(2, 1000001):
        if nt[i] and nt[nguoc(i)] and i != nguoc(i):
            cnt[i] = 1


if __name__ == '__main__':
    seive()
    ck()
    t = int(input())
    for _ in range(t):
        a = list([])
        n = int(input())
        for i in range(2, n):
            if cnt[i] and i not in a and nguoc(i) < n:
                a.append(i)
                a.append(nguoc(i))
        for x in a:
            print(x, end = ' ')
        print()