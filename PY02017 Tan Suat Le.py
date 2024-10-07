if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        d = dict([])
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for x in d:
            if d[x] % 2:
                print(x)
                break