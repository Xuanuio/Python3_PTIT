def wgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    n, k = map(int, input().split())
    cnt = 0
    for i in range(10 ** (k - 1), 10 ** k):
        if wgcd(i, n) == 1:
            print(i, end = " ")
            cnt += 1
            if cnt % 10 == 0:
                print()