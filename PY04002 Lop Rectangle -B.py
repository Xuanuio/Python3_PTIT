import sys

a = sys.stdin.read()
a = a.split()
a.insert(2,'1')

def input(): 
    return ' '.join(a[:3])

class Rectangle:
    def __init__(self, x, y, z) -> None:
        self.z = 1
        if x * y <= 0:
            print('INVALID')
            self.z = 0
        self.x = x
        self.y = y

    def perimeter(self):
        if self.z:
            return self.x * 2 + self.y * 2
        return ''

    def area(self):
        if self.z:
            return self.x * self.y
        return ''

    def color(self):
        if self.z:
            return a[-1].title()
        return ''

if __name__ == '__main__':
    # Not need Code because:
    # Xuanuio_uytin
    # Xuanuio_uytin
    # Xuanuio_uytin
    t_b = 'Không cần code đoạn này vì hàm Main sẽ tự đọng đc thay thế.'
    note = 'Nếu bạn muốn chạy test thì cứ paste code hàm main vào đây.'
    print(t_b, note, sep = '\n')