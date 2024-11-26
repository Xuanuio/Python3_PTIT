if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        i, j, l, ck = 0, 0, 0, 1
        while i < n and j < m and l < k:
            if a[i] == b[j] == c[l]:
                print(a[i], end=' ')
                ck = 0
                i += 1
                j += 1
                l += 1
            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[l]:
                j += 1
            else:
                l += 1
        if ck:
            print('NO')
        else:
            print()