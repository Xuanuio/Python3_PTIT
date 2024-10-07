from math import *

def nt(n):
    if n < 2:
        return 0
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return 0
    return 1

def nguoc(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def ck(n):
    while n != 0:
        r = n % 10
        if r != 2 and r != 3 and r != 5 and r != 7:
            return 0
        n //= 10
    return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if ck(n) and nt(n) and nguoc(n):
            print("Yes")
        else:
            print("No")       