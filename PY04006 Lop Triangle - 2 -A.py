from math import sqrt

if __name__ == '__main__':
    s = []
    t = int(input())
    for _ in range(t):
        s += list(map(float, input().split()))
    i = 0
    for _ in range(t):
        a = sqrt((s[i] - s[i + 2]) ** 2 + (s[i + 1] - s[i + 3]) ** 2)
        b = sqrt((s[i + 2] - s[i + 4]) ** 2 + (s[i + 3] - s[i + 5]) ** 2)
        c = sqrt((s[i + 4] - s[i]) ** 2 + (s[i + 5] - s[i + 1]) ** 2)
        if max(a, b, c) * 2 >= a + b + c:
            print('INVALID')
        else:
            area = sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4
            print(f'{area:.2f}')
        i += 6