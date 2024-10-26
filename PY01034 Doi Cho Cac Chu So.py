def find(s, i):
    ans = i
    for j in range(i + 1, len(s)):
        if s[j] < s[i]:
            if ans == i:
                ans = j
            elif s[ans] < s[j]:
                ans = j
    if s[ans] < s[i]:
        return ans
    return -1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        ans = ''
        for i in range(n - 1, -1, -1):
            idx = find(s, i)
            if idx > -1:
                ans = s[:i] + s[idx] + s[i + 1: idx] + s[i] + s[idx + 1:]
                break
        if ans != '' and ans != s and ans[0] != '0':
            print(ans)
        else:
            print(-1)