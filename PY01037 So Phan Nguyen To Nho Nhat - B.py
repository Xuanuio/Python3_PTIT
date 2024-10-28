import bisect
from sys import stdin
from math import isqrt

a = [1, 2, 4, 6, 12, 24, 36, 48, 60, 120, 180, 240, 360, 720, 840, 1260, 1680, 2520, 5040, 7560, 10080, 15120,
        20160, 25200, 27720, 45360, 50400, 55440, 83160, 110880, 166320, 221760, 277200, 332640, 498960, 554400,
        665280, 720720, 1081080, 1441440, 2162160, 2882880, 3603600, 4324320, 6486480, 7207200, 8648640, 10810800]

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(a[bisect.bisect_left(a, n)])

# def count(n):
#     cnt = 0
#     for i in range(1, isqrt(n)+1):
#         if n % i == 0:
#             cnt += 1
#             if i != n // i:
#                 cnt += 1
#     return cnt
#
# def sinh():
#     Max = 0
#     i = 1
#     while 1:
#         n = count(i)
#         if Max < n:
#             print(i)
#             Max = n
#             if i >= 10**7:
#                 break
#         i += 1
#
# sinh()  # -> list: a