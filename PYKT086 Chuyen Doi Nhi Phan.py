def solve(b, s):
    if b == 2:
        return s
    n = len(s)
    ans = ''
    if b == 4:
        if n % 2:
            s = '0' + s
            n += 1
        for i in range(n-1, -1, -2):
            sum = int(s[i]) + int(s[i-1]) * 2
            ans += str(sum)
        return ans[::-1]
    if b == 8:
        if n % 3:
            s = '0' * (3 - n % 3) + s
            n += 3 - n % 3
        for i in range(n-1, -1, -3):
            sum = int(s[i]) + int(s[i-1]) * 2 + int(s[i-2]) * 4
            ans += str(sum)
        return ans[::-1]
    if b == 16:
        if n % 4:
            s = '0' * (4 - n % 4) + s
            n += 4 - n % 4
        for i in range(n-1, -1, -4):
            sum = int(s[i]) + int(s[i-1]) * 2 + int(s[i-2]) * 4 + int(s[i-3]) * 8
            if sum < 10:
                ans += str(sum)
            else:
                ans += chr(ord('A') + sum - 10)
        return ans[::-1]

if __name__ == '__main__':
    a = []
    with open('DATA.in') as f:
        for line in f:
            a.append(line.strip())
    t = int(a[0])
    for i in range(1, t*2, 2):
        b = int(a[i])
        s = a[i+1]
        print(solve(b, s))