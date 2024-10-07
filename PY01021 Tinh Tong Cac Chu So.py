if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ans, sum = "", 0
        for i in s:
            if i.isdigit():
                sum += int(i)
            else:
                ans += i
        ans = ''.join(sorted(ans))
        if sum != 0:
            ans += str(sum)
        print(ans)