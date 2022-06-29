import sys
from collections import deque
input = sys.stdin.readline

c, r = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]
move = [[0, 1], [0, -1], [-1, 0], [1, 0]]

visited = []
for _ in range(r):
    visited.append([False] * c)

def bfs(x, y):
    my_team = board[x][y]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 0
    while q:
        x, y = q.popleft()
        count += 1
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < r and 0<= ny < c):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] != my_team:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    return count

team_dict = {'W':0, 'B':0}

for i in range(r):
    for j in range(c):
        if not visited[i][j]:
            team_dict[board[i][j]] += (bfs(i, j) ** 2)

print(team_dict['W'], team_dict['B'])
