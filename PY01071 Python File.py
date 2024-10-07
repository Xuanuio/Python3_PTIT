if __name__ == '__main__':
    s = input()
    n = len(s)
    if s[n-3] == '.' and s[n-2].lower() == 'p' and s[n-1].lower() == 'y':
        print("yes")
    else:
        print("no")