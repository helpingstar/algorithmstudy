import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline


def solution():
    n_size, n_pick = map(int, input().split())

    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

    board = [list(map(int, input().split())) for _ in range(n_size)]
    visited = [[False] * n_size for _ in range(n_size)]

    two_pos = []

    def bfs(x, y, cnt):
        visited[x][y] = True
        q = deque()
        q.append((x, y))
        while q:
            x, y = q.popleft()
            if board[x][y] == 2:
                two_pos.append((x, y, cnt))
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if not (0 <= nx < n_size and 0 <= ny < n_size):
                    continue
                if board[nx][ny] == 1:
                    continue
                if visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                q.append((nx, ny))

    def bfs2(idx_list):
        q = deque()
        bfs2_visited = [[False] * n_size for _ in range(n_size)]
        for idx in idx_list:
            r, c, _ = two_pos[idx]
            bfs2_visited[r][c] = True
            q.append((r, c, 0))
        while q:
            r, c, step = q.popleft()
            for dr, dc in delta:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < n_size and 0 <= nc < n_size):
                    continue
                if bfs2_visited[nr][nc]:
                    continue
                if board[nr][nc] == 1:
                    continue

                bfs2_visited[nr][nc] = True
                q.append((nr, nc, step + 1))
        return step
    
    cnt = 0
    for r in range(n_size):
        for c in range(n_size):
            if visited[r][c]:
                continue
            if board[r][c] == 1:
                continue
            cnt += 1
            bfs(r, c, cnt)
    ans = float('inf')
    for comb in combinations(range(len(two_pos)), n_pick):
        num_visited = [False] * (cnt + 1)
        visit_count = 0
        for n in comb:
            island = two_pos[n][2]
            if num_visited[island]:
                continue
            visit_count += 1
            num_visited[island] = True
            if visit_count == cnt:
                ans = min(ans, bfs2(comb))
                break
    
    print(-1 if ans == float('inf') else ans)

solution()
