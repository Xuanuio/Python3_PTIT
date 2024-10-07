if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ans = ""
        a = [x for x in s.split()]
        for x in a:
            if(len(ans) + len(x) <= 100):
                ans += x + " "
            else:
                break
        print(ans)