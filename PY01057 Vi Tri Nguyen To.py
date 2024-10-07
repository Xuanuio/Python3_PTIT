from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True

def ck(a):
    for i in range(len(a)):
        res = int(a[i])
        if nt(i) and nt(res) == False:
            return 0
        elif nt(i) == False and nt(res):
            return 0
    return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        if(ck(a)):
            print('YES')
        else:
            print('NO')