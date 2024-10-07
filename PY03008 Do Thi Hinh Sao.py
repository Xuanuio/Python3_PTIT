if __name__ == '__main__':
    cnt = 0
    d = dict([])
    t = int(input())
    for _ in range(t-1):
        n, m = map(int, input().split())
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
        if m not in d:
            d[m] = 1
        else:
            d[m] += 1
    for x, y in d.items():
        if y > 1:
            cnt += 1
    if cnt == 1:
        print("Yes")
    else:
        print("No")