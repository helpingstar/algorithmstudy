import sys
input = sys.stdin.readline

dr = (-1, -1, -1,  0, 0,  1, 1, 1)
dc = (-1,  0,  1, -1, 1, -1, 0, 1)

N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
board = [[5] * N for _ in range(N)]

trees = []
for _ in range(M):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    trees.append((z, x, y))

for i in range(K):
    new_trees = []
    dead_trees = []
    spread_trees = []
    # spring
    for age, r, c in sorted(trees):
        if age <= board[r][c]:
            board[r][c] -= age
            new_trees.append((age+1, r, c))
            if (age+1) % 5 == 0:
                spread_trees.append((r, c))
        else:
            dead_trees.append((age, r, c))
    # summer
    for age, r, c in dead_trees:
        board[r][c] += age // 2
    # fall
    for r, c in spread_trees:
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            new_trees.append((1, nr, nc))
    # winter
    for r in range(N):
        for c in range(N):
            board[r][c] += A[r][c]
    
    trees = new_trees
    
print(len(trees))