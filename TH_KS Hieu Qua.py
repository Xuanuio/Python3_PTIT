if __name__ == '__main__':
    a0, b0, c0 = map(int, input().split())
    a1, b1, c1 = map(int, input().split())
    start = a0 * 3600 + b0 * 60 + c0
    end = a1 * 3600 + b1 * 60 + c1
    if end >= start:
        kq = end - start
    else:
        kq = 86400 - start + end
    print(kq)