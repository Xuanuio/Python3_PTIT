if __name__ == '__main__':
    while True:
        t = int(input())
        if t == 0:
            break
        a = []
        for _ in range(t):
            a.append(int(input()))
        Min, Max = min(a), max(a)
        if Min == Max:
            print('BANG NHAU')
        else:
            print(Min, Max)