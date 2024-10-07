if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        a = s.split('.')
        if len(a) != 4:
            print('NO')
            continue
        ok = 1
        for x in a:
            if x.isnumeric() == 0 or int(x) < 0 or int(x) > 255:
                print('NO')
                ok = 0
                break
        if ok:
            print('YES')