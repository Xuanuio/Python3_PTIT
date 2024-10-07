from sys import stdin

if __name__ == '__main__':
    se = set({})
    for line in stdin:
        a = list(map(int, line.split()))
        for x in a:
            se.add(x % 42)
    print(len(se))