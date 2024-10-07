def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())
        print(gcd(a, b))