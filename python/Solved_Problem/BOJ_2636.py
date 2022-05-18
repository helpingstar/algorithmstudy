import sys
from collections import deque

input = sys.stdin.readline

move = ((0, -1), (0, 1), (-1, 0), (1, 0))

board = []
# visited = []

r, c = map(int, input().split())

# board 그리기
for _ in range(r):
    board.append(list(map(int, input().split())))
    # visited.append([False] * (c))


# bfs로 board를 탐색한다. 
# 0이면 deque에 집어넣고 추가 탐색을 계속하고
# 0이 아니라면 해당 장소를 0으로 바꾸고 visited에 넣는다. 
def bfs(x, y):
    q = deque()
    visited = set()
    q.append((x, y))

    num = 0

    while q:
        x, y = q.popleft()

        for dx, dy in move:
            nx = x + dx
            ny = y + dy

            # if visited[nx][ny]:
            #     continue
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if (nx, ny) in visited:
                continue
            
            visited.add((nx, ny))
            if board[nx][ny] == 0:
                q.append((nx, ny))
            else:
                board[nx][ny] = 0
                num += 1
    return num

cnt = 0
no_zero = 0

# bfs는 0이 아닌 장소의 개수를 리턴하기 때문에 
# 0을 리턴하면 모든 치즈가 "이미" 녹았다는 뜻이다
# 0이 아니라면 그 수를 no_zero에 저장한다.
while True:
    result = bfs(0, 0)

    if result == 0:
        break
    else:
        no_zero = result
        cnt += 1

print(cnt)
print(no_zero)
