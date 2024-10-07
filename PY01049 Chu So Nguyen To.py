from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def ck(a):
    n = 0
    if nt(len(a)) == False:
        print('NO')
    else:
        for i in range(len(a)):
            res = int(a[i])
            if nt(res):
                n += 1
        if n > len(a) // 2:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        ck(n)       