if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ans = ""
        n = len(s)
        cnt = 1
        s = s + "s"
        for i in range(n):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                ans = ans + str(cnt) + s[i]
                cnt = 1
        print(ans)