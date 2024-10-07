from math import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        kc = sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)
        return f'{kc:.4f}'
    
def Decimal(s):
    return float(s)

if __name__ == '__main__':
    print('Xuanuio_uytin')