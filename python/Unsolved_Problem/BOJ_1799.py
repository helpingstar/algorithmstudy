import sys

input = sys.stdin.readline

n = int(input())

board = []
zero_pos = []
ans = 0
re_board = [[] for _ in range(2*n-1)]
shop_list = [[-1, -1] for _ in range(2*n-1)]

for _ in range(n):
    board.append(list(map(int, input().split())))

for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            re_board[r-c + (n-1)].append((r, c))

def is_promising(x):
    nr, nc = shop_list[x]
    for i in range(x):
        er, ec = shop_list[i]
        if er == -1 and ec == -1:
            continue
        if (nr+nc) == (er+ec):
            return False
    return True

def dp(x, cnt):
    global ans
    global n
    if n == 1:
        if board[0][0] == 1:
            ans = 1
        else:
            ans = 0
    if x == 2*n-1:
        ans = max(cnt, ans)
        return
    else:
        # lower bound
        if (2*n-1 - x + cnt) > ans:
            for r, c in re_board[x]:
                shop_list[x] = [r, c]
                if is_promising(x):
                    dp(x+1, cnt+1)
            shop_list[x] = [-1, -1]
            dp(x+1, cnt)

dp(0, 0)

print(ans)
