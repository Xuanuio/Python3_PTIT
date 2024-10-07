import re

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        for s in re.split("[^a-z0-9]", input().lower()):
            a.append(s)
    d = dict([])
    for x in a:
        if x != '':
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
    for x in sorted(d, key = lambda x: (-d[x], x)):
        if d[x] >= k:
            print(x, d[x])