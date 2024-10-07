def partition(n, max_num, current, result):
    if n == 0:
        result.append(current.copy())
        return
    for i in range(min(n, max_num), 0, -1):
        current.append(i)
        partition(n - i, i, current, result)
        current.pop()

def solve(n):
    result = []
    partition(n, n, [], result)
    return result

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = solve(n)
        print(len(ans))
        for x in ans:
            print(f"({' '.join(map(str, x))})", end = ' ')
        print()