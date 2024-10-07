if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a, b = [], []
        for i in range(n):
            tmp = list(map(int, input().split()))
            a.append(tmp)
        for i in range(3):
            tmp = list(map(int, input().split()))
            b.append(tmp)
        s=0
        for i in range(n):
            if i==n-2:
                break
            for j in range(m):
                if j==m-2:
                    break
                for x in range(3):
                    for y in range(3):
                        s+=b[x][y]*a[i+x][j+y]
        print(s)