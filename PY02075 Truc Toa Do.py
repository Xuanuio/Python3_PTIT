def solve(a, n):
    a = sorted(a, key=lambda x: (x[1], x[0]))
    res = 1
    second = a[0][1]
    for i in range(1, n):
        if a[i][0] >= second:
            second = a[i][1]
            res += 1
    return res

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = []
        for i in range(n):
            tmp = [int(x) for x in input().split()]
            a.append(tmp)
        print(solve(a, n))