from sys import stdin

def check(n, v):
    for i in v:
        if i // n == i // (n + 1):
            return False
    return True

def solve():
    input = stdin.read
    data = input().split()
    
    index = 0
    
    n = int(data[index])
    index += 1
    a = [int(data[index + i]) for i in range(n)]
    index += n
    
    b = sorted(a)
    c = a[:]
    
    for i in range(b[0], 0, -1):
        if check(i, a):
            for j in range(n):
                c[j] = a[j] // (i + 1) + 1
            break
    
    res = sum(c)
    print(res)

if __name__ == '__main__':
    solve()