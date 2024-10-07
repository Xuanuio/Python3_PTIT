if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b, sum = [], sum(a)
    for i in range(n):
        sum = 0
        for j in range(n):
            if j != i:
                sum += abs(a[i] - a[j])
        b.append(sum)
    print(min(b), end = ' ')
    for i in range(n):
        if b[i] == min(b):
            print(a[i])
            break  