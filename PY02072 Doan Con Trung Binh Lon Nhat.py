if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    ans, curr = 0, 0

    for i in range(n):
        if a[i] == m:
            curr += 1
            ans = max(ans, curr)
        else:
            curr = 0

    print(ans)