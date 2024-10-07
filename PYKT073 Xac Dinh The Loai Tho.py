if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = list(input().split())
        a.append(len(b))
    s = ''.join(str(x) for x in a)
    s = s.replace('7777', '2')
    s = s.replace('68', '1')
    while '11' in s:
        s = s.replace('11', '1')
    print(len(s))
    for x in s:
        print(x)