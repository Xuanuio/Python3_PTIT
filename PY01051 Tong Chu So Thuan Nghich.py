def tong(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

def tn(n):
    if n < 10:
        return 0
    rev, m = 0, n
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == m

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if tn(tong(n)):
            print("YES")
        else:
            print("NO")