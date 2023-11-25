import sys
import heapq
input = sys.stdin.readline

def solution():
    N = int(input())
    q = []
    my = -int(input())
    if N == 1:
        print(0)
        return
    for _ in range(N-1):
        heapq.heappush(q, -int(input()))
    
    cnt = 0
    while my >= q[0]:
        temp = heapq.heappop(q)
        cnt += 1
        my -= 1
        heapq.heappush(q, temp+1)

    print(cnt)

solution()
    
    
    