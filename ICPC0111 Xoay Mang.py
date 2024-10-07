if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        s = a[m:] + a[:m]
        for x in s:
            print(x, end=' ')
        print()