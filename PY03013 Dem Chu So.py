def cnt(x, n):
    res = 0
    for i in range(0, 10):
        m = 10**i 
        if m > n: break
        a = n // m
        b = n % m
        z = a % 10
        if z > x: 
            res += ((a // 10) + 1) * m
        elif z == x: 
            res += (a // 10) * m + (b + 1)
        else: 
            res += (a // 10) * m
        if x == 0: 
            res -= m
    return res

def num(d, l, r):
    return cnt(d, r) - cnt(d, l - 1)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        for i in range(10):
            print(num(i, a, b), end = ' ')
        print()