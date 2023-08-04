import sys

input = sys.stdin.readline


def solution():
    C, R = map(int, input().split())
    K = int(input())
    if R * C < K:
        return 0

    cnt = 0
    pos = [0, 1]
    up = R
    right = C - 1
    down = R - 1
    left = C - 2
    while True:
        for u in range(up):
            pos[0] += 1
            cnt += 1
            if cnt == K:
                return pos
        up -= 2
        for r in range(right):
            pos[1] += 1
            cnt += 1
            if cnt == K:
                return pos
        right -= 2
        for d in range(down):
            pos[0] -= 1
            cnt += 1
            if cnt == K:
                return pos
        down -= 2
        for l in range(left):
            pos[1] -= 1
            cnt += 1
            if cnt == K:
                return pos
        left -= 2


ans = solution()
if ans == 0:
    print(0)
else:
    print(ans[1], ans[0])
