if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        dp = [-1]*n
        stack = []
        for i in range(n-1, -1, -1):
            if len(stack) == 0 or a[stack[-1]] >= a[i]:
                stack.append(i)
            else:
                while len(stack) > 0 and a[stack[-1]] < a[i]:
                    dp[stack[-1]] = i
                    stack.pop()
                stack.append(i)
        for i in range(n):
            print(i - dp[i], end=' ')
        print()