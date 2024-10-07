def tong(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(key=lambda x: (tong(x), x))
        for x in a:
            print(x, end=' ')
        print()