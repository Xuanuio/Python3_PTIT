def ck(s):
    f, n = s[0], len(s)
    if n % 2 == 0:
        return 0
    if f == s[1]:
        return 0
    for i in range(0, n, 2):
        if f != s[i]:
            return 0
    return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if ck(s):
            print("YES")
        else:
            print("NO")