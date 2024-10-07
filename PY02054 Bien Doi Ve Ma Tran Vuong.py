if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    if n == m:
        for i in range(n):
            b = list(map(int, input().split()))
            a.append(b)
        for i in range(n):
            for j in range(m):
                print(a[i][j], end=' ')
            print()
    elif n > m:
        cnt = n - m
        for i in range(n):
            b = list(map(int, input().split()))
            if i % 2 == 0 and cnt > 0:
                cnt -= 1
            else:
                a.append(b)
        for i in range(m):
            for j in range(m):
                print(a[i][j], end=' ')
            print()
    else:
        cnt = m - n
        for i in range(n):
            b = list(map(int, input().split()))
            a.append(b)
        for j in range(m):
            if j % 2 and cnt > 0:
                cnt -= 1
                for i in range(n):
                    a[i][j] = 2024
        for i in range(n):
            for j in range(m):
                if a[i][j] != 2024:
                    print(a[i][j], end=' ')
            print()