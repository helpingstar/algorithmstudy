import sys

def solution():
    input = sys.stdin.readline

    n_size, n_magic = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n_size)]
    magics = [tuple(map(int, input().split())) for _ in range(n_magic)]
    direction = ((0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
    water_copy_direction = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    cloud = [[n_size-1, 0], [n_size-1, 1], [n_size-2, 0], [n_size-2, 1]]
    visited = [[-1] * n_size for _ in range(n_size)]

    def water_copy(r, c):
        cnt = 0
        for dr, dc in water_copy_direction:
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < n_size and 0 <= nc < n_size):
                continue
            if board[nr][nc] > 0:
                cnt += 1
        return cnt

    for i, (d, s) in enumerate(magics):
        # move cloud
        for c in range(len(cloud)):
            cloud[c][0] = (cloud[c][0] + (direction[d][0] * s)) % n_size
            cloud[c][1] = (cloud[c][1] + (direction[d][1] * s)) % n_size
        # rain
        for cr, cc in cloud:
            board[cr][cc] += 1
        # water copy
        for cr, cc in cloud:
            board[cr][cc] += water_copy(cr, cc)
            visited[cr][cc] = i
        # new cloud
        cloud = []
        for r in range(n_size):
            for c in range(n_size):
                if visited[r][c] != i and board[r][c] >= 2:
                    cloud.append([r, c])
                    board[r][c] -= 2
    
    result = 0

    for i in range(n_size):
        result += sum(board[i])
    
    print(result)

solution()      