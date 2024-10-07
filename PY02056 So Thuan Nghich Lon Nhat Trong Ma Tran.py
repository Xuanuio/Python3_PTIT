def tn(n):
    s = str(n)
    if len(s) < 2:
        return 0
    return s == s[::-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    Max = -1
    for i in range(n):
        for j in range(m):
            if tn(a[i][j]) and a[i][j] > Max:
                Max = a[i][j]
    if Max == -1:
        print('NOT FOUND')
    else:
        print(Max)
        for i in range(n):
            for j in range(m):
                if a[i][j] == Max:
                    print('Vi tri [' + str(i) + '][' + str(j) + ']')