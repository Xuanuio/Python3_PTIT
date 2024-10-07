if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        if len(a) > len(b):
            print('NO')
            continue
        a.sort()
        b.sort()
        j = len(a) - 1
        for i in range(len(b)-1, 0, -1):
            if b[i] >= a[j]:
                j -= 1
    
        if j <= 0:
            print('YES')
        else:
            print('NO')