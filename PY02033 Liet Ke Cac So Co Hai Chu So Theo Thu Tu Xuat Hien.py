if __name__ == '__main__':
    s = input()
    n = len(s)
    if n % 2:
        n -= 1
    d = dict([])
    for i in range(0, n, 2):
        res = s[i] + s[i + 1]
        if res in d:
            d[res] += 1
        else:
            d[res] = 1
    for x in d:
        if d[x] != 0:
            print(x, end=' ')
            d[x] = 0