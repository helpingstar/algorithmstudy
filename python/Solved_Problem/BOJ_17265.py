import sys
from collections import deque

input = sys.stdin.readline

dx = (0, 1)
dy = (1, 0)

def calc(x, y, com):
    if com == '+':
        return x + y
    elif com == '-':
        return x - y
    else:
        return x * y

def solution():
    N = int(input())

    board = [list(input().split()) for _ in range(N)]
    
    # print(board)
    min_ans = float('inf')
    max_ans = -float('inf')
    q = deque()
    q.append((0, 1, int(board[0][0]), board[0][1]))
    q.append((1, 0, int(board[0][0]), board[1][0]))
    
    # print(board[0][1])
    
    while q:
        x, y, now, cal = q.popleft()
        # print(f'[debug] {x, y, now, cal}')
        if x == N-1 and y == N-1:
            min_ans = min(min_ans, now)
            max_ans = max(max_ans, now)
            continue
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if (nx + ny) % 2 == 0:
                # print(f'[debug] {nx, ny, now, cal}')
                q.append((nx, ny, calc(now, int(board[nx][ny]), cal), None))
            else:
                q.append((nx, ny, now, board[nx][ny]))
    return max_ans, min_ans

print(*solution())