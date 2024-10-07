if __name__ == '__main__':
    a = [x.lower() for x in input().split()]
    a = set(a)
    b = [x.lower() for x in input().split()]
    b = set(b)
    s1 = a.union(b)
    s2 = a.intersection(b)
    print(' '.join(sorted(s1)))
    print(' '.join(sorted(s2)))