import sys
import heapq

input = sys.stdin.readline

N, M, K = map(int, input().split())

dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

nutritions = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    n = int
    x, y, z = map(int, input().split())
    heapq.heappush(trees[x-1][y-1], z)

for _ in range(K):
    child = []
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                new_trees = []
                dead = 0
                while trees[r][c]:
                    age = heapq.heappop(trees[r][c])
                    if board[r][c] >= age:
                        board[r][c] -= age
                        age += 1
                        if age % 5 == 0:
                            child.append((r, c))
                        heapq.heappush(new_trees, age)
                    else:
                        dead += age // 2
                trees[r][c] = new_trees
                board[r][c] += dead
            board[r][c] += nutritions[r][c]
    for r, c in child:
        for i in range(8):
            nr = r + dx[i]
            nc = c + dy[i]

            if not (0 <= nr < N and 0 <= nc < N):
                continue
            heapq.heappush(trees[nr][nc], 1)

ans = 0
for r in range(N):
    for c in range(N):
        ans += len(trees[r][c])
print(ans)
