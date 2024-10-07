def dao(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

def wgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if wgcd(n, dao(n)) == 1:
            print("YES")
        else:
            print("NO")