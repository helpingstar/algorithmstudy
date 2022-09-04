import sys

input = sys.stdin.readline

board = [input().rstrip() for _ in range(5)]

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
answer = set()

def backtracking(arr: list, num: int, n_y: int):
    if n_y > 3:
        return
    if num == 7:
        arr.sort()
        answer.add(tuple(arr))
    else:
        adjacents = set()
        for x, y in arr:
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < 5 and 0 <= ny < 5):
                    continue
                if (nx, ny) in arr:
                    continue
                adjacents.add((nx, ny))
        for a_x, a_y in adjacents:
            if board[a_x][a_y] == 'Y':
                backtracking(arr + [(a_x, a_y)], num+1, n_y+1)
            else:
                backtracking(arr + [(a_x, a_y)], num+1, n_y)

for i in range(5):
    for j in range(5):
        if board[i][j] == 'S':
            backtracking([(i, j)], 1, 0)

print(len(answer))