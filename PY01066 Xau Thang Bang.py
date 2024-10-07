def ck():
    s = input()
    n = len(s)
    for i in range(1, (n + 3) // 2):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(s[n-i]) - ord(s[n-i-1])):
            return 0
    return 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        if ck():
            print("YES")
        else:
            print("NO")