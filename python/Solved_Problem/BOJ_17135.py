import sys
from itertools import combinations

input = sys.stdin.readline


def solution():
    ROW, COL, dist = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(ROW)]

    def find_closest_enemy(r, c, visited):
        nonlocal ROW, COL, dist, board
        for d in range(1, dist+1):
            sr = r
            sc = c - d
            for i in range(d):
                sr -= 1
                sc += 1
                if not (0 <= sr < ROW and 0 <= sc < COL):
                    continue
                if visited[sr][sc]:
                    continue
                if board[sr][sc] == 0:
                    continue
                return (sr, sc)
            for i in range(d-1):
                sr += 1
                sc += 1
                if not (0 <= sr < ROW and 0 <= sc < COL):
                    continue
                if visited[sr][sc]:
                    continue
                if board[sr][sc] == 0:
                    continue
                return (sr, sc)
        return (-1, -1)

    result = 0
    for comb in combinations(range(COL), 3):
        cnt = 0
        visited = [[False] * COL for _ in range(ROW)]
        for r_pos in range(ROW, 0, -1):
            check = set()
            for c_pos in comb:
                x, y = find_closest_enemy(r_pos, c_pos, visited)
                if x != -1:
                    check.add((x, y))
            for x, y in check:
                visited[x][y] = True
                cnt += 1
        result = max(result, cnt)
    return result


print(solution())
