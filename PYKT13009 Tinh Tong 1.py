MOD = 10**9 + 7

def Mul(a, b, m):
    a %= m
    b %= m
    tmp = int((a * b) / m)
    return (a * b - tmp * m) % m

def Pow(a, b):
    res = 1
    while b:
        if b & 1:
            res = Mul(res, a, MOD)
        a = Mul(a, a, MOD)
        b >>= 1
    return res

def solve(n, k):
    a = [1] * (k + 4)
    b = [1] * (k + 4)
    dp = [1] * (k + 4)
    
    tmp = k + 2
    for i in range(1, tmp + 1):
        a[i] = Mul(a[i - 1], n - i, MOD)
        b[tmp - i + 1] = Mul(b[tmp - i + 2], n - (tmp - i + 1), MOD)
        dp[i] = Mul(dp[i - 1], i, MOD)
    
    sum_ = 0
    res = 0
    for i in range(1, tmp + 1):
        sum_ += Pow(i, k)
        sum_ %= MOD
        x = Mul(sum_, a[i - 1], MOD)
        y = Mul(dp[i - 1], dp[k + 2 - i], MOD)
        z = Mul(b[i + 1], Pow(Mul(y, -1 if (k - i) & 1 else 1, MOD), MOD - 2), MOD)
        res = (res + Mul(x, z, MOD)) % MOD
    
    return (res + MOD) % MOD

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))