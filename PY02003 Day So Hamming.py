def sinh(a):
    for i in range(60):
        for j in range(38):
            for k in range(26):
                a.append(2**i * 3**j * 5**k)
    a.sort()

def bin_search(a, n):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == n:
            return m + 1
        elif a[m] < n:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':
    a = []
    sinh(a)
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = bin_search(a, n)
        if m != -1:
            print(m)
        else:
            print('Not in sequence')