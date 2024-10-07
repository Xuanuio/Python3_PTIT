if __name__ == '__main__':
    a = set({})
    with open("CONTACT.in", "r") as f:
        for x in f:
            a.add(x.strip().lower())
    for x in sorted(a):
        print(x)