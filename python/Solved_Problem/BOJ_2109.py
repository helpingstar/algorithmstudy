import sys
import heapq

input = sys.stdin.readline


def solution():
    N = int(input())
    if N == 0:
        return 0
    lectures = [tuple(map(int, input().split())) for _ in range(N)]
    lectures.sort(key=lambda x: (-x[1], -x[0]))
    end = lectures[0][1]
    cur = 0
    result = 0
    q = []
    for i in range(end, 0, -1):
        while cur < N and lectures[cur][1] >= i:
            heapq.heappush(q, -lectures[cur][0])
            cur += 1
        if q:
            result -= heapq.heappop(q)

    return result


print(solution())
