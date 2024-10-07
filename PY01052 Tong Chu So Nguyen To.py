from math import *

def tong(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

def nt(n):
    if n < 2:
        return 0
    for i in range (2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if nt(tong(n)):
            print("YES")
        else:
            print("NO")