from math import sqrt

def nt(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def ck(n):
    if nt(n):
        return 0
    l, r = 0, 0
    for i in range(n, 1, -1):
        if nt(i):
            l = i
            break
    for i in range(n, 20102):
        if nt(i):
            r = i
            break
    return min(r - n, n - l)

if __name__ == '__main__':
    n = input()
    a = list(map(int, input().split()))
    sum = 0
    for x in a:
        sum = max(ck(x), sum)
    print(sum)