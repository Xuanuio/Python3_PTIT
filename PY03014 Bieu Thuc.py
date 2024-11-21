if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a = input()
        stack = []
        cnt = 1
        for x in a:
            if x == '(':
                stack.append(cnt)
                print(cnt, end = ' ')
                cnt += 1
            elif x == ')':
                print(stack.pop(), end = ' ')
        print()
        