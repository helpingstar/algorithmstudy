import sys
from collections import deque

def solution():
    input = sys.stdin.readline

    N, Q = map(int, input().split())
    SIZE = 2 ** N
    board = [list(map(int, input().split())) for _ in range(SIZE)]
    magics = list(map(int, input().split()))
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    for s in magics:
        if s > 0:
            b_size = 2 ** s
            for r in range(0, SIZE, b_size):
                for c in range(0, SIZE, b_size):
                    for i in range(2 ** (s-1)):
                        top = r + i
                        left = c + i
                        r_size = b_size - 1 - (2 * i)
                        save = board[top][left:left + r_size]
                        for t in range(r_size):
                            board[top][left + t] = board[top+r_size-t][left]
                        for t in range(r_size):
                            board[top+r_size-t][left] = board[top+r_size][left+r_size-t]
                        for t in range(r_size):
                            board[top+r_size][left+r_size-t] = board[top+t][left+r_size]
                        for t in range(r_size):
                            board[top+t][left+r_size] = save[t]
        
        minus_list = []
        for a in range(SIZE):
            for b in range(SIZE):
                if board[a][b] == 0:
                    continue
                cnt = 0
                for i in range(4):
                    na = a + dr[i]
                    nb = b + dc[i]
                    if (not (0 <= na < SIZE and 0 <= nb < SIZE)) or board[na][nb] == 0:
                        cnt += 1
                if cnt > 1:
                    minus_list.append((a, b))
        for a, b in minus_list:
            board[a][b] -= 1

    n_sum = 0
    for line in board:
        n_sum += sum(line)
    print(n_sum)

    visited = [[False] * SIZE for _ in range(SIZE)]

    rock = 0

    for r in range(SIZE):
        for c in range(SIZE):
            if not visited[r][c] and board[r][c] != 0:
                cnt = 1
                visited[r][c] = True
                q = deque([(r, c)])
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dr[i]
                        ny = y + dc[i]

                        if not (0 <= nx < SIZE and 0 <= ny < SIZE):
                            continue
                        if visited[nx][ny]:
                            continue
                        if board[nx][ny] == 0:
                            continue

                        cnt += 1
                        q.append((nx, ny))
                        visited[nx][ny] = True
                rock = max(rock, cnt)
    print(rock)
                        
solution()