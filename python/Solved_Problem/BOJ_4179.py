import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def solution():
    R, C = map(int, input().split())
    fires = deque()
    sang = deque()
    board = []
    step = 0
    # visited = [[False] * C for _ in range(R)]
    for r in range(R):
        line = list(input().rstrip())
        board.append(line)
        for c, v in enumerate(line):
            if v == 'J':
                # visited[r][c] = True
                sang.append((r, c))
            elif v == 'F':
                fires.append((r, c))

    while sang:
        step += 1
        new_sang = deque()
        new_fires = deque()

        while fires:
            x, y = fires.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # print(nx, ny)
                if not (0 <= nx < R and 0 <= ny < C):
                    continue
                if board[nx][ny] in {'F', '#'}:
                    continue
                # print(f'[debug] fire nx ny {nx, ny}')
                board[nx][ny] = 'F'
                new_fires.append((nx, ny))

        # for i in board:
        #     print(*i)

        while sang:
            x, y = sang.popleft()
            # print(f'[debug] x, y : {x, y}')
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < R and 0 <= ny < C):
                    # print(f'[debug] {nx, ny}')
                    # for i in board:
                    #     print(*i)
                    return step
                if board[nx][ny] in {'F', '#', 'J'}:
                    continue
                board[nx][ny] = 'J'
                new_sang.append((nx, ny))

        fires = new_fires
        sang = new_sang

    return "IMPOSSIBLE"


print(solution())
