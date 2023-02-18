import sys
from collections import deque, defaultdict

hx = (-2, -2, -1, -1, 1, 1, 2, 2)
hy = (-1, 1, -2, 2, -2, 2, -1, 1)

dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
INF = int(1e7)
input = sys.stdin.readline

def solution():
    n = int(input())
    n_col, n_row  = map(int, input().split())
    
    board = [list(map(int, input().split())) for _ in range(n_row)]
    
    if (n_col, n_row) == (1, 1):
        return 0
    
    visited = [[[False for _ in range(n+1)] for _ in range(n_col)] for _ in range(n_row)]
    q = deque()
    q.append((0, 0, 1, n))
    visited[0][0][n] = True
    while q:
        x, y, cnt, h_cnt = q.popleft()
        
        if h_cnt > 0:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]

                if not (0 <= nx < n_row and 0 <= ny < n_col):
                    continue
                if board[nx][ny] == 1:
                    continue
                if visited[nx][ny][h_cnt-1]:
                    continue
                
                if (nx, ny) == (n_row-1, n_col-1):
                    return cnt
                
                q.append((nx, ny, cnt+1, h_cnt-1))
                visited[nx][ny][h_cnt-1] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < n_row and 0 <= ny < n_col):
                continue
            if board[nx][ny] == 1:
                continue
            if visited[nx][ny][h_cnt]:
                continue
            
            if (nx, ny) == (n_row-1, n_col-1):
                return cnt
            
            q.append((nx, ny, cnt+1, h_cnt))
            visited[nx][ny][h_cnt] = True
    return -1

print(solution())