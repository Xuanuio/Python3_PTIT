if __name__ == '__main__':
    s = input()
    k = int(input())
    n = len(s)
    if n % 2:
        n -= 1
    ok = 1
    d = dict([])
    for i in range(0, n, 2):
        res = s[i] + s[i + 1]
        if res in d:
            d[res] += 1
        else:
            d[res] = 1
    d = dict(sorted(d.items()))
    for x in d:
        if d[x] >= k:
            print(x, d[x])
            ok = 0
    if ok:
        print('NOT FOUND')