import queue

a = list([])

def ck(n):
    if len(str(n)) % 2:
        return 0
    s = str(n)
    return s == s[::-1]

def solve():
    q = queue.Queue()
    q.put(2)
    q.put(4)
    q.put(6)
    q.put(8)
    while True:
        x = q.get()
        if x >= 10000000:
            break
        q.put(x * 10 + 0)
        q.put(x * 10 + 2)
        if ck(x * 10 + 2):
            a.append(x * 10 + 2)
        q.put(x * 10 + 4)
        if ck(x * 10 + 4):
            a.append(x * 10 + 4)
        q.put(x * 10 + 6)
        if ck(x * 10 + 6):
            a.append(x * 10 + 6)
        q.put(x * 10 + 8)
        if ck(x * 10 + 8):
            a.append(x * 10 + 8)

if __name__ == '__main__':
    solve()
    t = int(input())
    for _ in range(t):
        n = int(input())
        for x in a:
            if x < n:
                print(x, end=" ")
        print()