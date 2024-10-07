if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    ok = 1
    while ok:
        ok = 0
        i = 1
        while i < len(a):
            if (a[i] + a[i - 1]) % 2 == 0:
                ok = 1
                a[i] = -1
                a[i - 1] = -1
                i += 2
            else :
                i += 1
        a = list(filter(lambda x : x != -1, a))
    print(len(a))