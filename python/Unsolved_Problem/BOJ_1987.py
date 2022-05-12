import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y):
    answer = 1
    q = set()
    q.add((x, y, board[x][y]))

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if not ((0 <= nx < r) and (0 <= ny < c)):
                continue
            if board[nx][ny] in ans:
                continue
            
            q.add((nx,ny,ans + board[nx][ny]))
            answer = max(answer, len(ans)+1)
    return answer


r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]


print(bfs(0, 0))