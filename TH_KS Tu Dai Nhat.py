if __name__ == '__main__':
    s = input().split(" ")
    ans = 0
    for i in s:
        ans = max(ans, len(i))
    for i in s:
        if len(i) == ans:
            print(i, ans)
            break