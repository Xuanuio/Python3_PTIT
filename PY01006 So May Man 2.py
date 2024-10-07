if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ok = True
        while n != 0:
            x = n % 10
            n //= 10
            if x != 4 and x != 7:
                ok = False
                break
        if ok == True:
            print("YES")
        else:
            print("NO")