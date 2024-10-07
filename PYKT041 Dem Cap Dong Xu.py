def answers(n):
    if n < 2:
        return 0
    return n * (n - 1) // 2

if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        s = input()
        b = [x for x in s]
        a.append(b)
    ans, cnt = 0, 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if a[i][j] == 'C':
                cnt += 1
        ans += answers(cnt)
    for j in range(n):
        cnt = 0
        for i in range(n):
            if a[i][j] == 'C':
                cnt += 1
        ans += answers(cnt)
    print(ans)