from sys import stdin

def solve(a, n):
    b = [[0] * (i + 1) for i in range(2001)]
    for i in range(1, 2001):
        b[i][0] = i + 1
        for j in range(1, i + 1):
            x = i // j
            if b[i][x] == 0:
                b[i][x] = j
    
    Min = min(a)
    resMin = float('inf')
    
    for i in range(Min + 1):
        check = True
        sum_val = 0
        for j in range(n):
            sum_val += b[a[j]][i]
            if b[a[j]][i] == 0:
                check = False
                break
        if check and sum_val < resMin:
            resMin = sum_val
    
    return resMin

if __name__ == '__main__':
    input = stdin.read
    data = input().split()
    
    n = int(data[0])
    a = [int(data[i + 1]) for i in range(n)]
    
    result = solve(a, n)
    print(result)