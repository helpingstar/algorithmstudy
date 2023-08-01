import sys
from collections import deque

input = sys.stdin.readline


def solution():
    N, K = map(int, input().split())
    belt = list(map(int, input().split()))
    on_pos = 0
    off_pos = N-1
    robots = deque()
    cnt = 0
    while True:
        cnt += 1
        # 1
        on_pos = (on_pos-1) % (2 * N)
        off_pos = (off_pos-1) % (2 * N)
        # 1-@
        if robots and robots[0] == off_pos:
            robots.popleft()
        # 2
        for i, pos in enumerate(robots):
            if belt[(pos+1) % (2 * N)] > 0 and (i == 0 or ((pos+1) % (2 * N) != robots[i-1])):
                belt[(pos+1) % (2 * N)] -= 1
                robots[i] = (robots[i] + 1) % (2 * N)
        if robots and robots[0] == off_pos:
            robots.popleft()
        # 3
        if belt[on_pos] > 0:
            belt[on_pos] -= 1
            robots.append(on_pos)
        # 4
        zero_cnt = 0
        for n in belt:
            if n == 0:
                zero_cnt += 1
        if zero_cnt >= K:
            return cnt


print(solution())
