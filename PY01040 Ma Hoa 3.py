def solve(s): 
    a = list(s[:len(s)//2])
    b = list(s[len(s)//2:]) 
    r1, r2 = 0, 0 
    for i in a: 
        r1 += ord(i) - 65 
    for i in b: 
        r2 += ord(i) - 65 
    for i in range(len(a)): 
        a[i] = chr((ord(a[i]) - 65 + r1) % 26 + 65) 
    for i in range(len(b)): 
        b[i] = chr((ord(b[i]) - 65 + r2) % 26 + 65) 
    for i in range(len(a)): 
        a[i] = chr((ord(a[i]) - 65 + ord(b[i]) - 65) % 26 + 65) 
    for i in a: 
        print(i, end = '') 
    print() 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        solve(s)