from sys import stdin

if __name__ == '__main__':
    n = int(input())
    a, c, l = [], [], []
    for line in stdin:
        b = list(map(int, line.split()))
        a.extend(b)
    for x in a:
        if x % 2:
            l.append(x)
        else:
            c.append(x)
    c.sort()
    l.sort(reverse = True)
    ci, lj = 0, 0
    for i in range(n):
        if a[i] % 2:
            print(l[lj], end=' ')
            lj += 1
        else:
            print(c[ci], end=' ')
            ci += 1