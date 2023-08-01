import sys
import heapq


def solution():
    input = sys.stdin.readline
    N = int(input())

    q = []
    for _ in range(N):
        line = list(map(int, input().split()))
        for num in line:
            heapq.heappush(q, num)
            if len(q) > N:
                heapq.heappop(q)
    print(q[0])


solution()
