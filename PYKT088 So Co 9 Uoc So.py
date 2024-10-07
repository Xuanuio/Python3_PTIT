from math import *

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solve(n):
    primes = []
    
    limit = int(isqrt(n)) + 1
    for i in range(2, limit):
        if is_prime(i):
            primes.append(i)
    
    count = 0
    
    for p in primes:
        if p**8 <= n:
            count += 1
    
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            if primes[i]**2 * primes[j]**2 <= n:
                count += 1
            else:
                break
    
    return count

if __name__ == '__main__':
    n = int(input())
    print(solve(n))