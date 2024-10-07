def ck(a):
    c, l = int(a[0]), 0
    for i in range (1, len(a)):
        res = int(a[i])
        if i % 2 == 0:
            if res != 0:
                c *= res
        else:
            l += res
    print(c, l, sep = ' ')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        ck(a)