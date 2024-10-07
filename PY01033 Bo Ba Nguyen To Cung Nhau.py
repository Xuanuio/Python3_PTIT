def wgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        for j in range(i, r + 1):
            if wgcd(i, j) == 1:
                for k in range(j, r + 1):
                    if wgcd(i, k) == 1 and wgcd(j, k) == 1:
                        print('(', i, ', ', j, ', ', k, ')', sep = "")