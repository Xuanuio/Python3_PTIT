if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        n, ok = len(s), 1
        for i in range(n):
            if s[i] > '2' or s[i] < '0':
                ok = 0
                break
        if ok:
            print("YES")
        else:
            print("NO")