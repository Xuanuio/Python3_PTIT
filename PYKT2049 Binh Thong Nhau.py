class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, u):
        if u == self.parent[u]:
            return u
        else:
            self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

if __name__ == '__main__':
    n = int(input())
    uf = UnionFind(100005)
    for _ in range(n):
        u, v, c = map(int, input().split())
        u = uf.find(u)
        v = uf.find(v)
        if c == 1:
            uf.union(u, v)
        elif c == 2:
            if u == v:
                print(1)
            else:
                print(0)