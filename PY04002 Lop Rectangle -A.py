class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def perimeter(self):
        return (self.width + self.height) * 2

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f'{self.perimeter()} {self.area()} {self.color.title()}'

a = list(input().split())
if int(a[0]) * int(a[1]) <= 0:
    print('INVALID')
else:
    r = Rectangle(int(a[0]), int(a[1]), a[2])
    print(r)