if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s, b, c, d = 1, 1, 1, 1
    s *= a[0] * a[1]
    b *= a[-1] * a[-2]
    c *= b * a[-3]
    d *= s * a[-1]
    print(max(s, b, c, d))