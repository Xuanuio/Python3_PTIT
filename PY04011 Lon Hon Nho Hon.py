from collections import defaultdict, deque
from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline())
    ke = defaultdict(list)
    v = defaultdict(int)
    mp = {}
    dem = 0
    for _ in range(n):
        s1, s2, s3 = stdin.readline().split()
        if s1 not in mp:
            dem += 1
            mp[s1] = dem
        if s3 not in mp:
            dem += 1
            mp[s3] = dem
        if s2 == ">":
            ke[mp[s1]].append(mp[s3])
            v[mp[s3]] += 1
        else:
            ke[mp[s3]].append(mp[s1])
            v[mp[s1]] += 1

    qe = deque()
    for i in range(1, dem + 1):
        if v[i] == 0:
            qe.append(i)

    cnt = 0
    while qe:
        x = qe.popleft()
        cnt += 1
        for neighbor in ke[x]:
            v[neighbor] -= 1
            if v[neighbor] == 0:
                qe.append(neighbor)

    if cnt == dem:
        print("possible")
    else:
        print("impossible")