def ck(n):
    c, l, r = n % 10, (n // 10) % 10, 0
    while n != 0:
        if r % 2 == 0:
            if n % 10 != c:
                return 0
        else:
            if n % 10 != l:
                return 0
        r += 1
        n //= 10
    return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if ck(n):
            print("YES")
        else:
            print("NO")