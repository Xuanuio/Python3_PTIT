import queue

def ck(s):
    cnt, n = 0, len(s)
    for i in range(len(s)):
        if s[i] == "2":
            cnt += 1
    return cnt > n // 2

a = []

def solve():
    q = queue.Queue()
    q.put("1")
    q.put("2")
    while True:
        s = q.get()
        if len(s) > 10:
            break
        if(ck(s)):
            a.append(s)
        q.put(s + "0")
        q.put(s + "1")
        q.put(s + "2")


if __name__ == '__main__':
    solve()
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(n):
            print(a[i], end = ' ')
        print()