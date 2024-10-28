if __name__ == '__main__':
    s = input()
    if len(s) % 3 == 1:
        s = '00' + s
    elif len(s) % 3 == 2:
        s = '0' + s
    n = len(s)
    for i in range(0, n, 3):
        x = int(s[i]) * 4 + int(s[i + 1]) * 2 + int(s[i + 2])
        print(x, end='')

#   n = int(input())
#   print(f"{n, 2):o}")