if __name__ == '__main__':
    a = [] 
    n = int(input())
    for _ in range(n): 
        a.append([int(x) for x in input().split()]) 
    if n == 2:
        print(1, a[0][1] - 1)
        exit()
    res = [] 
    res.append(int((a[0][1] + a[0][2] - a[1][2]) / 2)) 
    for i in range(1, n): 
        res.append(a[0][i] - res[0]) 
    for i in res: 
        print(i, end = ' ') 