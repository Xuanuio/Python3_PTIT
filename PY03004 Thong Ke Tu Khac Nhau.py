if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        b = input()
        for c in ",.?!:;()-/":
            b = b.replace(c, ' ')
        s = b.split()
        for x in s:
            a.append(x.lower())
    d = dict([])
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in sorted(d, key = lambda x: (-d[x], x)):
        print(x, d[x])             