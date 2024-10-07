if __name__ == '__main__':
    n, m = map(int, input().split())
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    a = list(a)
    b = list(b)
    ok = 1
    if len(a) != len(b):
        ok = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ok = 0
            break
    if ok:
        print('YES')
    else:
        print('NO')