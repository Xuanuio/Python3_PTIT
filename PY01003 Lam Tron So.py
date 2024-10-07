if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cs = len(str(n))
        if cs == 1: 
            print(n)
            continue
        ans, res, s = 0, 0, 0
        while cs > 1:
            cs -= 1
            r = n % 10 + res
            n //= 10
            s += 1
            if r < 5:
                res = 0
            else:
                res = 1
        ans = (n + res) * (10 ** s)
        print(ans)