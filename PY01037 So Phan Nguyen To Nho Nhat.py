from sys import stdin

a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 
    10080, 15120, 20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 
    332640, 498960, 554400, 665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 
    7207200, 8648640, 10810800, 14414400, 17297280]

if __name__ == '__main__':
    N = a[43]
    ans = [0] * (N+1)
    ans[0] = ans[1] = 1
    for i in range(1, 44):
        for j in range(a[i-1] + 1, a[i] + 1): 
            ans[j] = a[i]

    stdin.readline()
    while 1:
        try:
            n = int(stdin.readline())
            if n <= N:
                print(ans[n])
            else:
                for i in range(44,len(a)):
                    if n <= a[i]:
                        print(a[i])
                        break
        except:
            break