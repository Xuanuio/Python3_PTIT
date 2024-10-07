from math import *

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        m = s
        if len(s) > 4:
            m = s[-4:]
        n = 0
        for i in range(len(m)):
            n = n * 10 + int(m[i])
        if nt(n):
            print("YES")
        else:
            print("NO")        