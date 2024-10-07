from sys import stdin

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def chuyen_vi(self):
        rows, cols = len(self.matrix), len(self.matrix[0])
        other = [[self.matrix[i][j] for i in range(rows)] for j in range(cols)]
        return Matrix(other)

    def mul(self, other):
        rows_a, cols_a = len(self.matrix), len(self.matrix[0])
        rows_b, cols_b = len(other.matrix), len(other.matrix[0])
        result = [[0] * cols_b for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                result[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(cols_a))
        return Matrix(result)

    def out(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

if __name__ == '__main__':
    s = [int(x) for line in stdin for x in line.split()]
    t = s[0]
    i = 1
    for _ in range(t):
        n, m = s[i], s[i + 1]
        i += 2
        a = [s[i + j * m:i + (j + 1) * m] for j in range(n)]
        i += n * m
        mt = Matrix(a)
        cv = mt.chuyen_vi()
        ans = mt.mul(cv)
        ans.out()