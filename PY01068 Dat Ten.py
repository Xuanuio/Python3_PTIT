from itertools import combinations

if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(input().split())
    se = sorted(set(a))
    s = combinations(se, k)
    for x in s:
        print(' '.join(str(i) for i in x))