nt = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def solve(l, r, n):
    chan, le = 0, 0
    if (r - l + 1) % 2 == 0:
        chan = (r - l + 1) // 2
        le = chan
    else:
        if l % 2:
            chan = (r - l + 1) // 2
            le = chan + 1
        else:
            le = (r - l + 1) // 2
            chan = le + 1
    return str(chan) + ' ' + str(le)


if __name__ == '__main__':
    while 1:
        a = [int(x) for x in input().split()]
        if a[0] == -1:
            break
        l, r = a[0], a[1]
        n = int(input())
        print(solve(l, r, n))