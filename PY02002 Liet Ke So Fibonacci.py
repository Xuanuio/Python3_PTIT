fibo = [0] * 93

def fb():
    fibo[1] = 1
    fibo[2] = 1
    for i in range(3, 93):
        fibo[i] = fibo[i-1] + fibo[i-2]

if __name__ == '__main__':
    fb()
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            print(fibo[i], end = ' ')
        print()