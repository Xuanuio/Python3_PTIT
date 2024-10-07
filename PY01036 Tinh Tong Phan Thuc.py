if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = 0.000000
        for i in range(n, 0, -2):
            s += 1 / i
        print('{:.6f}'.format(s))