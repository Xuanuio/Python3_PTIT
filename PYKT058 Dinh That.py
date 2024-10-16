def check(ke, u, v, e, n):
    q, used = [u], [0] * (n + 1)
    used[u] = 1
    while q:
        x = q.pop()
        if x == v:
            return False
        for i in ke[x]:
            if used[i] == 0 and i != e:
                q.append(i)
                used[i] = 1
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, u, v = map(int, input().split())
        ke = {x: [] for x in range(1, n + 1)}
        for _ in range(m):
            x, y = map(int, input().split())
            ke[x].append(y)
            ke[y].append(x) 

        cnt = 0
        for i in range(1, n + 1):
            if i != u and i != v:
                if check(ke, u, v, i, n):
                    cnt += 1
        print(cnt)