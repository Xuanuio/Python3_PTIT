def Try(n, start, end, middle):
    if n == 1:
        print(start, '->', end)
    else:
        Try(n - 1, start, middle, end)
        Try(1, start, end, middle)
        Try(n - 1, middle, end, start)

if __name__ == '__main__':
    n = int(input())
    Try(n, 'A', 'C', 'B')