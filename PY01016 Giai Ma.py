if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        f = 0
        c = ""
        for i in range(n):
            if i % 2 == 1:
                f = int(s[i])
                while f != 0:
                    f -= 1
                    c = c + s[i-1]
        print(c)