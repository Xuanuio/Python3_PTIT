from math import *

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

def sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    t = int(input())
    while t != 0:
        t -= 1
        n, m = map(int, input().split())
        if nt(sum(gcd(n, m))) == 1:
            print("YES")
        else:
            print("NO")     