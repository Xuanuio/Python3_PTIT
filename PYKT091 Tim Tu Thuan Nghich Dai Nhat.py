def tn(s):
    return s == s[::-1]

if __name__ == '__main__':
    f1 = open("VANBAN.in", "r")
    a = []
    d = dict([])
    cnt = 0

    for line in f1:
        for word in line.split():
            if tn(word):
                a.append(word)
                cnt = max(cnt, len(word))

    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1

    for x in a:
        if len(x) == cnt and d[x] > 0:
            print(x, d[x])
            d[x] = 0

    f1.close()