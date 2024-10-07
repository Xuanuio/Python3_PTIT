def power_mod(a, b, M):
    result = 1
    a = a % M
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % M
        b = b // 2
        a = (a * a) % M
    return result

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, d, M = map(int, input().split())
        res = power_mod(a, b, M)
        res = power_mod(res, c, M)
        res = power_mod(res, d, M)
        print(res)  