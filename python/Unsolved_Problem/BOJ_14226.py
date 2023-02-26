import sys
from collections import deque
import heapq

input = sys.stdin.readline

def solution():
    target = int(input())
    visited = dict()
    visited[1] = 0
    q = []
    heapq.heappush(q, (0, 1))
    while q:
        step, now = heapq.heappop(q)
        # print(f'[debug] step, now : {step, now}')
        if now == target:
            return step
        cnt = 2
        while now * cnt <= 2000 and (now*cnt not in visited or step +cnt < visited[now*cnt]):
            # print(f'[debug] gob : {now*cnt}')
            visited[now*cnt] = step + cnt
            heapq.heappush(q, (step + cnt, now*cnt))
            cnt += 1
        
        cnt = 1
        while now - cnt >= 2 and (now - cnt not in visited or step + cnt < visited[now-cnt]):
            visited[now-cnt] = step + cnt
            heapq.heappush(q, (step + cnt, now -cnt))
            cnt += 1
        

print(solution())