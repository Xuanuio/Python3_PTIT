if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        n = len(s)
        ok = True
        for i in range(n-1):
            if s[i+1] < s[i]:
                ok = False
                break
        if ok == True:        
            print("YES")
        else: 
            print("NO")