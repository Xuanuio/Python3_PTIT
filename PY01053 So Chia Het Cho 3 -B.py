def tong(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if tong(n) % 3 == 0:
            print("YES")
        else:
            print("NO")