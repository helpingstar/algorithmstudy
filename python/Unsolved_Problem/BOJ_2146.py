import sys
from collections import deque, defaultdict

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

region = defaultdict(list)

# 섬을 구분해주는 bfs
def bfs1(i, j, count):
    q = deque()
    q.append([i, j])
    visited[i][j] = True
    board[i][j] = count
    region[count].append((i, j))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue
            if board[nx][ny] == 1:
                visited[nx][ny] = True
                board[nx][ny] = count
                q.append([nx, ny])
                region[count].append((nx, ny))

# 바다를 건너며 가장 짧은 거리를 구한다.
def bfs2(my_region):
    global answer
    dist = [[-1] * n for _ in range(n)] # 거리가 저장될 배열
    # my_region의 땅 리스트

    q = deque(region[my_region])
    for i, j in region[my_region]:
        dist[i][j] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 갈 수 없는 곳이면 continue
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if board[nx][ny] > 0 and board[nx][ny] != my_region:
                return dist[x][y]
            # 바다를 만나면 dist를 1씩 늘린다.
            if board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append([nx, ny])


n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
count = 1
answer = sys.maxsize

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            bfs1(i, j, count)
            count += 1

# print(board)

# 갖고 있는 개수만큼
for my_region in range(1, count):
    answer = min(answer, bfs2(my_region))

print(answer)
