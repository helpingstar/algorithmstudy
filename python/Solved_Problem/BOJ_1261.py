"""
왜 이게 다익스트라 문제인지 모르겠다.
아마 각 대륙을 라벨링하고 거리를 구한 뒤에 0,0 -> m,n 의 거리를 다익스트라로 구하는 것 같다

bfs로 탐색하며 다음 공간이 0일때 지금보다 다음이 작거나 같다면 continue (지금 >= 다음)
지금보다 다음이 크다면 현재값을 다음 note에 기록한다. (지금 < 다음)
다음 공간이 1이면 지금 + 1 보다 다음이 작거나 같다면 continue (지금 +1 >= 다음)
지금+1 보다 다음이 크다면 현재값을 다음 note에 기록한다. (지금 + 1 < 다음)
기록한 위치가 note에 기록됬다면 기록한 해당 위치를 덱(큐)에 넣는다.
"""

import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

input = sys.stdin.readline

c, r = map(int, input().split())

INF = c*r # 그냥 큰 수

board = [] # 원본 행렬
note = []  # 허문 벽 기록하는 행렬
for _ in range(r):
    board.append(list(input().rstrip()))
    note.append([INF] * c)

note[0][0] = 0 # 시작지점

def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if board[nx][ny] == '0':
                if note[x][y] >= note[nx][ny]:
                    continue
                note[nx][ny] = note[x][y]
            else:           # board[nx][ny] == 1
                if note[x][y] + 1 >= note[nx][ny]:
                    continue
                note[nx][ny] = note[x][y] + 1
            q.append((nx, ny))

bfs(0, 0)

print(note[r-1][c-1])
