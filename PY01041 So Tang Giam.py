if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        if n < 3:
            print("NO")
            continue
        Max, pos, ok = s[0], 0, 1
        for i in range(n-1):
            if s[i] < s[i+1]:
                Max = s[i+1]
                pos = i + 1
            else:
                break
        for i in range(pos, n-1):
            if s[i] <= s[i+1]:
                ok = 0
                break
        if ok:
            print("YES")
        else:
            print("NO")