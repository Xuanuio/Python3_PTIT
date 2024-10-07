class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __add__(self, other):
        return SoPhuc(self.thuc + other.thuc, self.ao + other.ao)
    
    def __mul__(self, other):
        return SoPhuc(self.thuc * other.thuc - self.ao * other.ao, self.thuc * other.ao + self.ao * other.thuc)
    
    def out(self):
        if self.ao < 0:
            print(f'{self.thuc} - {-self.ao}i', end = '')
        else:
            print(f'{self.thuc} + {self.ao}i', end = '')

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a, b, c, d = map(int, input().split())
        sp1 = SoPhuc(a, b)
        sp2 = SoPhuc(c, d)
        ans1 = sp1 + sp2
        ans1 *= sp1
        ans1.out()
        print(', ', end = '')
        ans2 = sp1 + sp2
        ans2 *= ans2
        ans2.out()
        print()