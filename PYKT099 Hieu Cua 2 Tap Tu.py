if __name__ == '__main__':
    a, b = set(), set()
    
    with open("DATA1.in", "r") as f1:
        for line in f1:
            for x in line.split():
                a.add(x.lower())
    
    with open("DATA2.in", "r") as f2:
        for line in f2:
            for x in line.split():
                b.add(x.lower())
    
    d1 = sorted(a - b)
    d2 = sorted(b - a)
    
    print(' '.join(d1))
    print(' '.join(d2))