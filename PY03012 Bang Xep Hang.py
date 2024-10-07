class member:
    def __init__(self, name, ac, sub):
        self.name = name
        self.ac = ac
        self.sub = sub

    def __str__(self):
        return f'{self.name} {self.ac} {self.sub}'

if __name__ == '__main__':
    a = []
    t = int(input())
    for _ in range(t):
        name = input()
        ac, sub = map(int, input().split())
        a.append(member(name, ac, sub))
    a.sort(key = lambda x: (-x.ac, x.sub, x.name))
    for x in a:
        print(x)