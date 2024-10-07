if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, m = map(float, input().split())
        s = 0
        while True:
            if m - n * ((1 + x / 100) ** s) < 0:
                break
            else: 
                s += 1
        print(s)