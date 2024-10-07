if __name__ == '__main__':
    n = int(input())
    s = [input().strip() for _ in range(n)]
    idx = [0]

    for i in range(1, n):
        if '?' not in s[i] and s[i] != '' and s[i-1] == '':
            idx.append(i)

    idx.append(n+1)

    for i in range(len(idx) - 1):
        print(s[idx[i]] + ': ' + str(idx[i+1] - idx[i] - 2))