class ThiSinh:
    def __init__(self, id, ten, team, school):
        self.id = 'C' + format(id, '03d')
        self.ten = ten
        self.team = team
        self.school = school

    def get_ten(self):
        return self.ten
    
    def __str__(self):
        return f'{self.id} {self.ten} {self.team} {self.school}'

if __name__ == '__main__':
    n = int(input())
    a, b = [], []
    b.append(['Xuanuio'])
    for _ in range(n):
        c = []
        c.append(input())
        c.append(input())
        b.append(c)
    t = int(input())
    for i in range(t):
        x, y = input(), input()
        z = int(y[-2:])
        ts = ThiSinh(i+1, x, b[z][0], b[z][1])
        a.append(ts)
    a.sort(key=lambda x: x.get_ten())
    for ts in a:
        print(ts)     