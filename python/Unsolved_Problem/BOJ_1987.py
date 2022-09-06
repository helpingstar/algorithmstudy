import sys

input = sys.stdin.readline
r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
answer = 0

def bfs(x, y):
    answer = 1
    q = set()
    q.add((x, y, board[x][y]))

    while q:
        x, y, ans = q.pop()

        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if board[nx][ny] in ans:
                continue

            q.add((nx, ny, ans + board[nx][ny]))
            answer = max(answer, len(ans) + 1)
    return answer

print(bfs(0, 0))