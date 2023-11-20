import sys
from collections import deque

input = sys.stdin.readline

def solution():
    n_row, n_col = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(n_row)]
    visited = [[False] * n_col for _ in range(n_row)]
    move = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def bfs(sr, sc):
        color = board[sr][sc]
        q = deque()
        q.append((sr, sc, -1, -1))
        while q:
            r, c, pr, pc = q.popleft()
            for dr, dc in move:
                nr = r + dr
                nc = c + dc
                if (nr, nc) == (pr, pc):
                    continue
                if not (0 <= nr < n_row and 0 <= nc < n_col):
                    continue
                if board[nr][nc] != color:
                    continue
                if visited[nr][nc]:
                    return True
                visited[nr][nc] = True
                q.append((nr, nc, r, c))
        return False
    
    for r in range(n_row):
        for c in range(n_col):
            if visited[r][c]:
                continue
            if bfs(r, c):
                print('Yes')
                return
    print('No')

solution()