if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        d = dict([])
        for _ in range(n):
            x = int(input())
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        Max, ans = 0, 0
        for i in sorted(d.keys()):
            if d[i] > Max:
                Max = d[i]
                ans = i
        print(ans)