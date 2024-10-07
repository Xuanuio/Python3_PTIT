def solve():
    h, m, s = map(int, input().split())
    if not (0 <= h < 12) or not (0 <= m < 60) or not (0 <= s < 60):
        return
    else:
        ang = 30 * h + 0.5 * m + (1 / 120) * s
        print(f"Angle: {ang}")

if __name__ == '__main__':
    solve()