if __name__ == '__main__':
    m = int(input())
    v = int(input())
    t = int(input())
    d = input()
    if d == "C":
        result = (v * t) % m
    else:
        result = (m - (v * t) % m) % m
    print(result)