def tich(n):
    s = 1
    while n != 0:
        r = n % 10
        if r != 0:
            s *= r
        n //= 10
    return s

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(tich(n))