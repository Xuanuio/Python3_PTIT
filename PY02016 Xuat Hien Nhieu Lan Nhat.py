if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        d = dict([])
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        Max, ans = 0, 0
        for i in sorted(d.keys()):
            if d[i] > Max:
                Max = d[i]
                ans = i
        if Max > n // 2:
            print(ans)
        else:
            print("NO")