if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        l, r = 0, 0
        r = n % 100
        s = len(str(n))
        s -= 2
        l = n // (10 ** s)
        if l == r:
            print("YES")
        else:
            print("NO")