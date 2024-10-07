if __name__ == '__main__':
    while True:
        tmp = input()
        if len(tmp) < 3:
            break
        k, s = tmp.split()
        t = int(k)
        n = len(s)
        c, ans = "", ""
        p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
        for i in range(n):
            if s[i] >= 'A' and s[i] <= 'Z':
                r = (ord(s[i]) - ord('A') + t) % 28
            elif s[i] == '_':
                r = (26 + t) % 28
            else: 
                r = (27 + t) % 28
            c = c + p[r]
        for j in range(n, 0, -1):
            ans = ans + c[j-1]
        print(ans)