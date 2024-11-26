if __name__ == '__main__':
    a = []
    t = int(input())
    for i in range(t):
        b = input()
        a.append(b)
    while len(a) > 0:
        idx = len(a)
        for i in range(len(a)):
            if a[i] == '':
                idx = i
                break
        print(f'{a[0]}: {idx - 1}')
        a = a[idx+1:]