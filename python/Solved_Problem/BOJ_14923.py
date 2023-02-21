import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = int(1e7)
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def solution():
    R, C = map(int, input().split())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(R)]
    visited = set()
    q = []
    visited.add((sx-1, sy-1, 1))
    heapq.heappush(q, (0, sx-1, sy-1, 1))
    while q:
        step, x, y, magic = heapq.heappop(q)
        # print(f'[debug] {step, x, y, magic}')
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            if nx == ex-1 and ny == ey-1:
                return step + 1
            if (nx, ny, magic) in visited:
                continue
            
            if board[nx][ny] == 1 and magic == 0:
                continue
            
            if board[nx][ny] == 1:
                heapq.heappush(q, (step+1, nx, ny, 0))
                visited.add((nx, ny, 0))
                
            else:
                heapq.heappush(q, (step+1, nx, ny, magic))
                visited.add((nx, ny, magic))
    return -1
print(solution())