if __name__ == '__main__':
    s = input()
    k = int(input())
    n = len(s)
    if n % 2:
        n -= 1
    a, ok = [], 1
    for i in range(0, n, 2):
        a.append(int(s[i:i + 2]))
    d = dict([])
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = sorted(d.items(), key=lambda x: x[0])
    for x in d:
        if x[1] >= k:
            print(x[0], x[1])
            ok = 0
    if ok:
        print("NOT FOUND")