if __name__ == '__main__':
    s = input()
    n = len(s)
    if n % 2:
        n -= 1
    a = set({})
    for i in range(0, n, 2):
        res = s[i] + s[i + 1]
        a.add(res)
    print(' '.join(sorted(a)))