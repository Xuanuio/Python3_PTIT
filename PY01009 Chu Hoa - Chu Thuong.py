if __name__ == '__main__':
    s = input()
    n = int(len(s))
    t, h = 0, 0
    for i in range(n):
        if s[i].islower():
            t += 1
        else: 
            h += 1
    if h > t:
        print(s.upper())
    else:
        print(s.lower())