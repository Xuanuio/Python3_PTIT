if __name__ == '__main__':
    a = []
    with open("DATA.in", "r") as f1:
        for line in f1:
            for x in line.split():
                if not x.isdigit() or int(x) > 2147483647:
                    a.append(x)
    a.sort()
    for x in a:
        print(x, end = ' ')