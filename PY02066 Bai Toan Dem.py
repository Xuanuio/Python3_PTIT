from sys import stdin

if __name__ == '__main__':
    n = int(input())
    a = []
    for line in stdin:
        b = list(map(int, line.split()))
        for x in b:
            a.append(x)
    a.sort()
    Max = max(a)
    ok = 1
    for x in range(Max):
        if x + 1 not in a:
            print(x + 1)
            ok = 0
    if ok:
        print('Excellent!')
