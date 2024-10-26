dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    a, ck = [], []
    cnt = 0
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
        ck.append([0] * m)
    for i in range(n):
        for j in range(m):
            if a[i][j] == -1:
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < n and 0 <= y < m and ck[x][y] == 0:
                        cnt += a[x][y]
                        ck[x][y] = 1
    print(cnt)