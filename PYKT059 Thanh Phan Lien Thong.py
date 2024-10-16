if __name__ == '__main__':
    n, m, x = map(int, input().split())
    ke = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        ke[a].append(b)
        ke[b].append(a)
    
    used = [0] * (n + 1)
    q = [x]
    used[x] = 1
    
    while q:
        u = q.pop()
        for v in ke[u]:
            if not used[v]:
                q.append(v)
                used[v] = 1
    
    check = True
    for i in range(1, n + 1):
        if not used[i]:
            check = False
            print(i)
    
    if check:
        print(0)