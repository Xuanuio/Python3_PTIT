def cmp(a, b):
    if a[1] == b[1]:
        return a[0] - b[0]
    return b[1] - a[1]

def solve():
    n, m = map(int, input().split())
    mp = {}
    a = list(map(int, input().split()))
    for x in a:
        if x in mp:
            mp[x] += 1
        else:
            mp[x] = 1

    v = list(mp.items())
    v.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    Max = v[0][1]
    secondMax = -1
    for it in v:
        if it[1] < Max:
            secondMax = it[1]
            break

    ok = False
    for it in v:
        if it[1] == secondMax:
            print(it[0], end=" ")
            ok = True

    if not ok:
        print("NONE")

if __name__ == "__main__":
    solve()