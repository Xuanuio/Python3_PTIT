from math import *

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return 0
    return 1

def ck(n):
    sum, s = 0, str(n)
    for i in range(len(s)):
        if (i % 2) != (int(s[i]) % 2):
            return 0
        sum += int(s[i])
    if nt(sum):
        return 1
    else:
        return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if ck(n):
            print("YES")
        else:
            print("NO")