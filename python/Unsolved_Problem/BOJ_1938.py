import sys
from collections import deque

input = sys.stdin.readline
INF = 10000
n = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]

board = [list(input().rstrip()) for _ in range(n)]

start = []
end = []

for r in range(n):
    for c in range(n):
        if board[r][c] == 'B':
            start.append([r, c])
        elif board[r][c] == 'E':
            end.append([r, c])

if start[0][0] == start[1][0]:
    b_vertical = 1
else:
    b_vertical = 0

if end[0][0] == end[1][0]:
    e_vertical = 1
else:
    e_vertical = 0

b_pos = start[1]
e_pos = end[1]

# status : (horizontal, vertical)
memory = []

for i in range(n):
    memory.append([[0, 0] for _ in range(n)])

def bfs(start, end, vertical):
    q = []
    q.append((start, vertical, 0))
    while q:
        st, v, cost = q.popleft()
        x, y = st
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if v:
                if not (0 <= nx < n and 1 <= nx < n-1):
                    continue
                
                    

