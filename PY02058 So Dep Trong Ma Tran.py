if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    Min, Max = 10**9, -1
    for _ in range(n):
        b = list(map(int, input().split()))
        Min = min(Min, min(b))
        Max = max(Max, max(b))
        a.append(b)
    lucky_number = Max - Min
    ok = 1
    for i in range(n):
        for j in range(m):
            if a[i][j] == lucky_number:
                if ok:
                    print(lucky_number)
                    ok = 0
                print('Vi tri [' + str(i) + '][' + str(j) + ']')
    if ok:
        print('NOT FOUND')