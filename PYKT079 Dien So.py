if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        l, r = min(a), max(a)
        cnt = 0
        for x in range(l, r+1):
            if x not in a:
                cnt += 1
        print(cnt)