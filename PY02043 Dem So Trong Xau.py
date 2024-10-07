if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        t = input()
        n, m = len(s), len(t)
        s = s.replace(t, '')
        n -= len(s)
        print(n // m)