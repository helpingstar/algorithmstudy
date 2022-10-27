import sys

input = sys.stdin.readline

h, w = map(int, input().split())
board = [list(map(int, list(input().rstrip()))) for _ in range(h)]
ans = 0

# 0: 오른쪽 방향, 1: 세로 방향
for i in range(1 << (h*w)):
    total = 0
    for r in range(h): # 세로 탐색
        s_col = 0
        for c in range(w): # 오른쪽 방향으로
            idx = r * w + c
            if ((i & (1 << idx)) == 0): # 오른쪽 방향일떄
                s_col = s_col * 10 + board[r][c]
            else:
                total += s_col
                s_col = 0
        total += s_col

    for c in range(w): # 가로 탐색
        s_row = 0
        for r in range(h): # 아래 방향으로
            idx = r * w + c
            if (i & (1 << idx) == 0): # 오른쪽 방향일 때
                total += s_row
                s_row = 0
            else:
                s_row = s_row * 10 + board[r][c]
        total += s_row

    ans = max(total, ans)

print(ans)
