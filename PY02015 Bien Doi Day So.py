if __name__ == '__main__':
    while 1:
        a, b, c, d = map(int, input().split())
        if a == b == c == d == 0:
            break
        cnt = 0
        if a == b == c == d:
            print(cnt)
            continue
        while a != b or b != c or c != d:
            a, b, c, d = abs(a-b), abs(b-c), abs(c-d), abs(d-a)
            cnt += 1
        print(cnt)