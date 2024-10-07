if __name__ == '__main__':
    a, k, n = map(int, input().split())
    b = k - a % k
    ck = 1 
    for i in range(a + b, n + 1, k):
        print(i - a, end = ' ') 
        ck = 0
    if(ck):
        print(-1)