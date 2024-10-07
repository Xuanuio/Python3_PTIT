if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        t = input()
        i, j = len(s), len(t)
        s = s.replace(t, "")
        ans = (i - len(s)) // j
        print(ans)