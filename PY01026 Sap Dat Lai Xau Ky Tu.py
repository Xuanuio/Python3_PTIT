if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print("Test ", i+1, ": ", sep="", end="")
        s1 = input()
        s2 = input()
        a = "".join(sorted(s1))
        b = "".join(sorted(s2))
        if a == b:
            print("YES")
        else:
            print("NO")