import sys

input = sys.stdin.readline

T = int(input())

def solution(x1, y1, r1, x2, y2, r2):
    distance = ((x1-x2) ** 2 + (y1-y2) ** 2) ** 0.5

    if distance > (r1 + r2):
        return 0

    if distance == (r1 + r2):
        return 1

    if distance < (r1 + r2):
        if distance + min(r1, r2) < max(r1, r2):
            return 0
        elif distance + min(r1, r2) == max(r1, r2):
            if distance == 0:
                return -1
            else:
                return 1
        else:
            return 2


for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(solution(x1, y1, r1, x2, y2, r2))
