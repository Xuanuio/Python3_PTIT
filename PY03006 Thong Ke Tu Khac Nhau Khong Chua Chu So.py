import re

if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        for s in re.split("[^a-z]", input().lower()):
            a.append(s)
    d = dict([])
    for x in a:
        if x != '':
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
    for x in sorted(d, key = lambda x: (-d[x], x)):
        print(x, d[x])