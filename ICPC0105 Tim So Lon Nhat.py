import re

if __name__ == '__main__':
    t = int(input())
    for t in range(t):
        s = input()
        print(max(int(i) for i in re.findall(r'\d+', s)))