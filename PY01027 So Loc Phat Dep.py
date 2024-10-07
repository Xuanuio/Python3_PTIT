def ck(s):
    s = s.replace('888', '1')
    for x in s:
        if x != '6' and x != '8':
            return False
    return True

if __name__ == '__main__':
    s = input()
    if ck(s):
        print('YES')
    else:
        print('NO')