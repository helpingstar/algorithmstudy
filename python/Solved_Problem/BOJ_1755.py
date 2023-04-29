import sys
import math
input = sys.stdin.readline

W, H, X, Y, P = map(int, input().split())

def check(a, b):
    if 0 <= a <= W and 0 <= b <= H:
        return True

    if math.sqrt(a ** 2 + (b - H/2) ** 2) <= H/2:
        return True

    if math.sqrt((a - W) ** 2 + (b - H/2) ** 2) <= H/2:
        return True

    return False

ans = 0

for _ in range(P):
    a, b = map(int, input().split())

    a -= X
    b -= Y

    if check(a, b):
        ans += 1
        # print(f'[debug] {a, b}')

print(ans)
