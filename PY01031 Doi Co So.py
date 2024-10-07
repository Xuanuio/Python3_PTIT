if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, b = map(int, input().split())
        stack = []
        while n != 0:
            stack.append(n % b)
            n //= b
        while len(stack) > 0:
            a = stack.pop()
            if a < 10:
                print(a, end='')
            else:
                print(chr(a + 55), end='')
        print()