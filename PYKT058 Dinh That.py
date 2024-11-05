def check(ke, u, v, e, n):
    q, un = [u], [0] * (n + 1)
    un[u] = 1
    while len(q) > 0:
        x = q.pop()
        if x == v:
            return False
        for i in ke[x]:
            if un[i] == 0 and i != e:
                q.append(i)
                un[i] = 1
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, u, v = map(int, input().split())
        ke = {x: [] for x in range(1, n + 1)}
        # ke = {}
        # for x in range(1, n + 1):
        #     ke[x] = []
        for i in range(m):
            x, y = map(int, input().split())
            ke[x].append(y)
        cnt = 0
        for i in range(1, n + 1):
            if i != u and i != v:
                if check(ke, u, v, i, n):
                    cnt += 1
        print(cnt)