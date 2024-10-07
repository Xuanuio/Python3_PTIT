if __name__ == '__main__':
    n = int(input())
    s = str(n)
    t = len(s)
    ans, kq, cnt = "" , "" , 0
    for i in range(t-1, -1, -1):
        ans += s[i]
        cnt += 1
        if cnt % 3 == 0 and cnt < t:
            ans += ','
    for j in range(len(ans)):
        kq += ans[len(ans)-1-j]
    print(kq)