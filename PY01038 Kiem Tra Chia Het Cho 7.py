def nguoc(n):
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 7 == 0:
            print(n)
            continue

        Xuanuio = 25052004
        x = Xuanuio - 25052024 + 1020
        
        while x != 0:
            x -= 1
            s = n + nguoc(n)
            if s % 7 == 0:
                print(s)
                break
            n = s
        else:
            print(-1)