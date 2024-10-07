def find_pivot_elements(a, n):
    max_left = [0] * n
    min_right = [0] * n
    
    max_left[0] = float('-inf')
    for i in range(1, n):
        max_left[i] = max(max_left[i-1], a[i-1])
    
    min_right[n-1] = float('inf')
    for i in range(n-2, -1, -1):
        min_right[i] = min(min_right[i+1], a[i+1])
    
    pivot_count = 0
    for i in range(n):
        if max_left[i] <= a[i] < min_right[i]:
            pivot_count += 1
    
    return pivot_count

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split())) 
        print(find_pivot_elements(a, n))