class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def chuyen_vi(self):
        other = [[0 for _ in range(len(self.matrix))] for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                other[j][i] = self.matrix[i][j]
        return Matrix(other)

    def mul(self, other):
        result = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(result)

    def out(self):
        for row in self.matrix:
            print(' '.join(map(str, row)))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = []
        for _ in range(n):
            b = list(map(int, input().split()))
            a.append(b)
        mt = Matrix(a)
        cv = mt.chuyen_vi()
        ans = mt.mul(cv)
        ans.out()