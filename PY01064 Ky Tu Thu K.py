def solve(n, k):
    mid = 2 ** (n - 1)
    if k == mid:
        return chr(ord('A') + n - 1)
    elif k < mid:
        return solve(n - 1, k)
    else:
        return solve(n - 1, k - mid)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(solve(n, k))
