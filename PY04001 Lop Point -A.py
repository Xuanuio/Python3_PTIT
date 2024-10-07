from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        kc = sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return f'{kc:.4f}'

t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(float, input().split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print(p1.distance(p2))