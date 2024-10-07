if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for x in a:
        if x + 1 not in a:
            print(x + 1)
            break