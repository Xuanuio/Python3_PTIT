if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = list(map(int, input().split()))
        Max, s = max(a), []
        for i in range(n):
            if a[i] == Max:
                s = a[:i] + [m] + a[i:]
                break
        am, duong = [], []
        for i in range(n + 1):
            if s[i] < 0:
                am.append(s[i])
            else:
                duong.append(s[i])
        print(*am, end=' ')
        print(*duong)