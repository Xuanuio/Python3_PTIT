if __name__ == '__main__':
    while 1:
        n = int(input())
        if n == 0:
            break
        cnt = 1
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            cnt += 1
        print(cnt)