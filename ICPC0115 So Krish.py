from math import *

def ck(n):
    m = n
    sum = 0
    while m > 0:
        sum += factorial(m % 10)
        m //= 10
    return sum == n

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if ck(n):
            print("Yes")
        else:
            print("No")