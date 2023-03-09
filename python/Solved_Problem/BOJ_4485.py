import sys
import heapq
input = sys.stdin.readline
INF = int(1e6)

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def solution(n):
    board = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = board[0][0]
    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    while q:
        step, x, y = heapq.heappop(q)
        if distance[x][y] < step:
            continue

        # print(step, x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if nx == n-1 and ny == n-1:
                return step + board[n-1][n-1]

            cost = step + board[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))


cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(f'Problem {cnt}: {solution(n)}')
    cnt += 1
