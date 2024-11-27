n, k = map(int,input().split()) 
a = [int(i) for i in input().split()] 
a.sort() 
cnt = 1 
for i in range(n - 1): 
    if a[i + 1] - a[i] > k: 
        cnt += 1 
print(cnt) 