from itertools import permutations

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        res = ""
        for i in range(1, n+1):
            res += str(i)
        s = permutations(res)
        a = []
        for i in s:
            tmp = ''.join(i)
            a.append(tmp)
        print(len(a))
        for i in range(len(a)-1, -1, -1):
            print(a[i], end = ' ')
        print()