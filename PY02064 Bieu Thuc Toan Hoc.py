def find(i):
    if i % 5 == 0:
        return 5
    if i % 5 == 1:
        return 1
    if i % 5 == 2:
        return -2
    if i % 5 == 3:
        return 3
    if i % 5 == 4:
        return -4

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        dp = [[0] * (n + 1) for i in range(5 * k + 1)]
        for i in range(1, 5 * k + 1):
            x = find(i)
            dp[i][i] = x * a[i] + dp[i - 1][i - 1]
            for j in range(i + 1, n + 1):
                dp[i][j] = max(dp[i][j - 1], x * a[j] + dp[i - 1][j - 1])
        print(dp[5 * k][n])