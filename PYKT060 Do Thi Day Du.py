def ck(zones, graph):
    for zone in zones:
        for v1 in zone:
            for v2 in zone:
                if v1 != v2:
                    if graph[v1][v2] == 0 or graph[v2][v1] == 0:
                        return False
    return True

def solve():
    n, m = int(input()), int(input())
    zones = []
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    par = [-1] * (n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x][y] = graph[y][x] = 1
        zone_index = par[x] if par[y] == -1 else par[y]
        if zone_index == -1:
            zones.append(set([x, y]))
            par[x] = par[y] = len(zones) - 1
        else:
            zones[zone_index].add(x)
            zones[zone_index].add(y)
            par[x] = par[y] = zone_index

    if ck(zones, graph):
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    solve()