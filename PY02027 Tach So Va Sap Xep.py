import re

if __name__ == "__main__":
    n = int(input())
    a = []
    for _ in range(n):
        s = input()
        b = [int(x) for x in re.split("[a-zA-Z]", s) if x]
        a.extend(b)
    a.sort()
    for x in a:
        print(x)