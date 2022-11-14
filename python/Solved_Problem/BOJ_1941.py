import sys

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

board = [list(input().rstrip()) for _ in range(5)]

ans = 0
check = set()

def dp(arr, crew, Y):
    global ans

    if tuple(sorted(arr)) in check:
        return
    check.add(tuple(sorted(arr)))

    if crew == 7:
        ans += 1
        # 여기서 return을 안해서 crew가 7일때 끝내지 않아서 시간초과가 일어남
        return

    next_pos = []

    for x, y in arr:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            if (nx, ny) in arr:
                continue
            next_pos.append((nx, ny))

    for nx, ny in next_pos:
        if board[nx][ny] == 'S':
            dp(arr + [(nx, ny)], crew + 1, Y)
        else:
            if Y < 3:
                dp(arr + [(nx, ny)], crew + 1, Y+1)


for r in range(5):
    for c in range(5):
        if board[r][c] == 'S':
            dp([(r, c)], 1, 0)

print(ans)
