if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    k, sum = int(input()), 0
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                sum += a[i][j]
            elif i + j > n - 1:
                sum -= a[i][j]
    sum = abs(sum)
    if sum <= k:
        print('YES')
    else:
        print('NO')
    print(sum)