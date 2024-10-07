from math import *

def nt(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    max_prime = -1
    for i in range(n):
        for j in range(m):
            if nt(a[i][j]) and a[i][j] > max_prime:
                max_prime = a[i][j]
    if max_prime == -1:
        print('NOT FOUND')
    else:
        print(max_prime)
        for i in range(n):
            for j in range(m):
                if a[i][j] == max_prime:
                    print('Vi tri [' + str(i) + '][' + str(j) + ']')