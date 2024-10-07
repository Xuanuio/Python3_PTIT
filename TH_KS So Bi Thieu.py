def check(n):
    if n <= 1:
        return
    a = []
    for i in range(n - 1):
        so = int(input())
        a.append(so)
    a = sorted(a)
    for i in range(n):
        if a[i] != i + 1:
            print(i + 1)
            break

if __name__ == '__main__':
    n = int(input())
    check(n)