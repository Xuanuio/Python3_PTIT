if __name__ == '__main__':
    t = int(input())
    se = set({})
    for _ in range(t):
        s = input()
        se.add(s)
    print(len(se))