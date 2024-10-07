if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        x, y, z = map(int, input().split())
        dp = [0] * (n + 1)
        dp[1] = x
        for i in range(2, n + 1):
            if i % 2:
                dp[i] = min(dp[i - 1] + x, dp[(i + 1) // 2] + z + y)
            else:
                dp[i] = min(dp[i - 1] + x, dp[i // 2] + z)
        print(dp[n])