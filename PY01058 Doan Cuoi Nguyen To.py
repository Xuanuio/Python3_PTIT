from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def ck(a):
    if len(a) < 4:
        s = int(a) 
    else:
        s = int(a[len(a)-4:])
    if nt(s):
            print('YES')
    else:
            print('NO') 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        ck(a)