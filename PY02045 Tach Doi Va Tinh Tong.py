if __name__ == '__main__':
    s = input()
    n = len(s)
    sum = 25052004
    while sum >= 10:
        l, r = int(s[:n // 2]), int(s[n // 2:])
        sum = l + r
        s = str(sum)
        n = len(s)
        print(sum)
    