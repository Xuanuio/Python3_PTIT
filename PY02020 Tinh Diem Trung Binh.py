if __name__ == '__main__':
    n = int(input())
    a = list(map(float, input().split()))
    
    Min , Max , sum = 10.0, 0.0, 0.0
    for i in a:
        sum += i
        if i < Min:
            Min = i
        if i > Max:
            Max = i
    
    for i in a:
        if i == Max:
            sum -= Max
            n -= 1
        if i == Min:
            sum -= Min
            n -= 1
    
    print('%.2f' % (sum / n))