import sys
from collections import deque, defaultdict
input = sys.stdin.readline

INF = int(1e10)

def solution():
    start, end = map(int, input().split())
    visited = defaultdict(lambda: INF)
    if start == end:
        return [start]
    q = deque()
    q.append((start, [start]))
    while q:
        now, track = q.popleft()
        if now + 1 == end:
            return track + [now + 1]
        if now * 2 == end:
            return track + [now * 2]
        if now > 0 and now - 1 == end:
            return track + [now-1]
        
        if len(track) + 1 < visited[now+1]:
            visited[now+1] = len(track) + 1
            q.append((now+1, track + [now + 1]))
        if len(track) + 1 < visited[now * 2]:
            visited[now*2] = len(track) + 1
            q.append((now*2, track + [now * 2]))
        if now > 0 and (len(track) + 1 < visited[now-1]):
            visited[now-1] = len(track) 
            q.append((now-1, track + [now - 1]))

result = solution()
print(len(result) - 1)
print(*result)