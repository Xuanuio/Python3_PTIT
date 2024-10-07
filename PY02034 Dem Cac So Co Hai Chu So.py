if __name__ == '__main__':
    s = input()
    n = len(s)
    if n % 2:
        n -= 1
    a = []
    for i in range(0, n, 2):
        a.append(int(s[i:i + 2]))
    d = dict([])
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for x in a:
        if d[x] != 0:
            print(x, d[x])
            d[x] = 0