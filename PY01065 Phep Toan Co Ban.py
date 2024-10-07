def calc(a, op, b, c):
    if op == '+':
        return a + b == c
    elif op == '-':
        return a - b == c
    elif op == '*':
        return a * b == c
    elif b != 0 and a % b == 0:
        return a // b == c
    else:
        return False

def xuly(s):
    ans = []
    if s.isdigit():
        ans.append(s)
    if s == '??':
        for i in '123456789':
            for j in '0123456789':
                ans.append(i + j)
    elif s[0] == '?':
        for i in '123456789':
            ans.append(i + s[1])
    elif s[1] == '?':
        for i in '0123456789':
            ans.append(s[0] + i)
    return ans

def tt(s):
    if s in '+-*/':
        return [s]
    return ['+', '-', '*', '/']

def solve(s):
    a, op, b, e, c = s.split()
    m1, m2, m3, m4 = [], [], [], []
    m1 = xuly(a)
    m2 = tt(op)
    m3 = xuly(b)
    m4 = xuly(c)
    for x in m1:
        for y in m2:
            for z in m3:
                for t in m4:
                    if calc(int(x), y, int(z), int(t)):
                        print(f'{x} {y} {z} = {t}')
                        return
    print('WRONG PROBLEM!')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        Xuanuio = input()
        solve(Xuanuio)