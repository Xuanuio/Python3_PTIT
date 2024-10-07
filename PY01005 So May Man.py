if __name__ == '__main__':
    x = int(input())
    cnt = 0
    while x != 0:
        r = x % 10
        x //= 10
        if r == 4 or r == 7:
            cnt += 1
    if cnt == 4 or cnt == 7:
        print("YES")
    else: 
        print("NO")