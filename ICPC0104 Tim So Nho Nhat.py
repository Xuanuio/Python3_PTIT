if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        s = input()
        s = s + 's'
        ans = 10 ** 20
        res = 0
        for i in range(len(s)) :
            if s[i].isalpha() :
                if i != 0 and s[i - 1].isdigit() : ans = min(ans, res)
                res = 0
            else : res = res * 10 + int(s[i])
        print(ans)