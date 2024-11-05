import re

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        for s in re.split("[^a-z0-9]", input().lower()):
            if s != '':
                a.append(s)
    d = dict([])
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x in sorted(d, key = lambda x: (-d[x], x)):
        print(x, d[x])             