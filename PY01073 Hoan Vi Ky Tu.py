from itertools import permutations

if __name__ == '__main__':
    s = input()
    res = permutations(s)
    for i in res:
        print("".join(i))