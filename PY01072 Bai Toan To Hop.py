from itertools import combinations

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(set(a))
    b.sort()
    res = combinations(b, m)
    for i in res:
        print(" ".join(map(str, i)))