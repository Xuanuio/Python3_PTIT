if __name__ == '__main__':
    s1, s2 = input(), input()
    n = int(input())
    n -= 1
    s = s1[:n] + s2 + s1[n:]
    print(s)