import sys
import heapq

input = sys.stdin.readline
T = int(input())


def solution():
    n = int(input())
    min_q = []
    max_q = []
    already_out = [False] * n
    for i in range(n):
        a, b = input().split()
        b = int(b)
        if a == 'I':
            heapq.heappush(min_q, (b, i))
            heapq.heappush(max_q, (-b, i))
        else:
            if b == 1:
                while max_q and already_out[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    _, idx = heapq.heappop(max_q)
                    already_out[idx] = True
            else:
                while min_q and already_out[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    _, idx = heapq.heappop(min_q)
                    already_out[idx] = True
    while min_q and already_out[min_q[0][1]]:
        heapq.heappop(min_q)
    while max_q and already_out[max_q[0][1]]:
        heapq.heappop(max_q)
    if not min_q:
        return 'EMPTY'
    else:
        return -max_q[0][0], min_q[0][0]

            
for _ in range(T):
    result = solution()
    if result == 'EMPTY':
        print(result)
    else:
        print(*result)