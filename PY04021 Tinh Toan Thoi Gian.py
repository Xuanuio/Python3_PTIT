class GameThu:
    def __init__(self, id, ten, vao, ra):
        self.id = id
        self.ten = ten
        self.vao = vao
        self.ra = ra

    def thoi_gian(self):
        ra = int(self.ra[:2]) * 60 + int(self.ra[3:])
        vao = int(self.vao[:2]) * 60 + int(self.vao[3:])
        return ra - vao
    
    def ck(self):
        h = self.thoi_gian() // 60
        m = self.thoi_gian() % 60
        print(self.id + ' ' + self.ten, end = ' ')
        print(f'{h} gio {m} phut')

if __name__ == '__main__':
    a = []
    n = int(input())
    for _ in range(n):
        gt = GameThu(input(), input(), input(), input())
        a.append(gt)
    a.sort(key = lambda x: -x.thoi_gian())
    for x in a:
        x.ck()