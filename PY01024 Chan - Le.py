def tong(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    if sum % 10 == 0:
        return 1
    else: 
        return 0

def ck(n):
    r = n % 10
    n //= 10
    while n != 0:
        m = n % 10
        if r - 2 != m and r + 2 != m:
            return 0
        r = m
        n //= 10
    return 1
            
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if tong(n) and ck(n):
            print("YES")
        else:
            print("NO")