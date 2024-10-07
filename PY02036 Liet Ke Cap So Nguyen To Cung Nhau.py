def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n-1):
        for j in range(i+1, n):
            if gcd(a[i], a[j]) == 1:
                print(a[i], a[j])