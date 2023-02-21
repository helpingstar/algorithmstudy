import sys
import heapq

input = sys.stdin.readline

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def solution():
    R, C, cnt = map(int, input().split())
    board = [list(map(int, input().rstrip())) for _ in range(R)]
    q = []
    heapq.heappush(q, (0, 0, 1, cnt))
    visited = set()
    visited.add((0, 0, cnt))
    while q:
        x, y, step, cnt = heapq.heappop(q)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < R and 0 <= ny < C):
                continue
            
            if nx == R-1 and ny == C-1:
                return step + 1
            
            if board[nx][ny] == 1 and cnt == 0:
                continue
            
            if board[nx][ny] == 1:
                if (nx, ny, cnt-1) not in visited:
                    visited.add((nx, ny, cnt-1))
                    heapq.heappush(q, (nx, ny, step+1, cnt-1))
            else:
                if (nx, ny, cnt) not in visited:
                    visited.add((nx, ny, cnt))
                    heapq.heappush(q, (nx, ny, step+1, cnt))
    return -1

print(solution())