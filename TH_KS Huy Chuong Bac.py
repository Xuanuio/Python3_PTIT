if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        x = int(input().strip())
        a.append(x)
    a.sort()
    print(f'Silver = {a[-2]}')