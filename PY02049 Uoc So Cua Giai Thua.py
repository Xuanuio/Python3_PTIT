if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = 0
        for i in range(k, n + 1, k):
            x = i
            while x % k == 0: 
                s += 1
                x //= k 
        print(s)