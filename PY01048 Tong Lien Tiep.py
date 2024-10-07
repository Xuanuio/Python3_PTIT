def solve(n):
    cnt, k = 0, 2
    while k * (k - 1) // 2 < n:
        if (n - (k * (k - 1) // 2)) % k == 0:
            cnt += 1
        k += 1
    return cnt

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve(n))
