if __name__ == '__main__':
    s = input()
    cnt = 0
    while(len(s) != 1):
        cnt += 1
        s = str(sum([int(ord(x) - 48) for x in s]))
    if cnt == 0:
        cnt += 1
    print(cnt)      