import sys
import math
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solution():
    sx, sy, tx, ty = map(int, input().split())
    n_planet = int(input())
    answer = 0

    for _ in range(n_planet):
        x, y, r = map(int, input().split())
        to_s = dist(sx, sy, x, y)
        to_t = dist(tx, ty, x, y)

        if (to_s - r) * (to_t - r) < 0:
            answer += 1
    return answer


for _ in range(int(input())):
    print(solution())
