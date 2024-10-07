from queue import Queue

def ck(s):
    if len(s) >= 10 or len(s) <= 3:
        return False
    if '2' not in s or '3' not in s or '5' not in s or '7' not in s:
        return False
    if s[-1] == '2':
        return False
    return True
        

if __name__ == '__main__':
    n = int(input())
    q = Queue()
    for digit in ['2', '3', '5', '7']:
        q.put(digit)
    a = []
    while not q.empty():
        x = q.get()
        if ck(x):
            a.append(x)
        if len(x) < n:
            for digit in ['2', '3', '5', '7']:
                q.put(x + digit)
    for x in a:
        print(x)