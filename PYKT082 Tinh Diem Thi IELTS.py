def lr(n):
    if n == 40 or n == 39:
        return 9.0
    if n == 38 or n == 37:
        return 8.5
    if n == 36 or n == 35:
        return 8.0
    if n == 34 or n == 33:
        return 7.5
    if n <= 32 and n >= 30:
        return 7.0
    if n <= 29 and n >= 27:
        return 6.5
    if n <= 26 and n >= 23:
        return 6.0
    if n <= 22 and n >= 20:
        return 5.5
    if n <= 19 and n >= 16:
        return 5.0
    if n <= 15 and n >= 13:
        return 4.5
    if n <= 12 and n >= 10:
        return 4.0
    if n <= 9 and n >= 7:
        return 3.5
    if n == 6 or n == 5:
        return 3.0
    if n == 4 or n == 3:
        return 2.5
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(float, input().split())
        a //= 1
        b //= 1
        a = lr(a)
        b = lr(b)
        n = a + b + c + d
        n /= 4
        if n - int(n) < 0.25:
            n = int(n) + 0.0
        elif n - int(n) < 0.75:
            n = int(n) + 0.5
        else:
            n = int(n) + 1.0
        print('%.1f' % n)