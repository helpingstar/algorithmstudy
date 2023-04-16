import sys

input = sys.stdin.readline
ans = 1
N = int(input())

board = [list(input().rstrip()) for _ in range(N)]

for c in range(N-1):
    for r in range(N):
        for left, right in [(board[r][c+1], board[r][c]), (board[r][c], board[r][c+1])]:
            left_cnt = 1
            delta = 1
            while r - delta >= 0 and board[r-delta][c] == left:
                delta += 1
                left_cnt += 1
            delta = 1
            while r + delta < N and board[r+delta][c] == left:
                delta += 1
                left_cnt += 1

            right_cnt = 1
            delta = 1
            while r - delta >= 0 and board[r-delta][c+1] == right:
                delta += 1
                right_cnt += 1
            delta = 1
            while r + delta < N and board[r+delta][c+1] == right:
                delta += 1
                right_cnt += 1

            l_cnt = 1
            delta = 1
            while c - delta >= 0 and board[r][c-delta] == left:
                delta += 1
                l_cnt += 1
            delta = 1
            while c + delta < N and board[r][c+delta] == left:
                delta += 1
                l_cnt += 1

            r_cnt = 1
            delta = 1
            while c - delta >= 0 and board[r][c-delta] == right:
                delta += 1
                r_cnt += 1
            delta = 1
            while c + delta < N and board[r][c+delta] == right:
                delta += 1
                r_cnt += 1
            if max(left_cnt, right_cnt, l_cnt, r_cnt) == 4:
                print(r, c)

            ans = max(ans, left_cnt, right_cnt, l_cnt, r_cnt)

for r in range(N-1):
    for c in range(N):
        for up, down in [(board[r][c], board[r+1][c]), (board[r+1][c], board[r][c])]:

            up_cnt = 1
            delta = 1
            while c - delta >= 0 and board[r][c-delta] == up:
                delta += 1
                up_cnt += 1
            delta = 1
            while c + delta < N and board[r][c+delta] == up:
                delta += 1
                up_cnt += 1

            down_cnt = 1
            delta = 1
            while c - delta >= 0 and board[r+1][c-delta] == down:
                delta += 1
                down_cnt += 1
            delta = 1
            while c + delta < N and board[r+1][c+delta] == down:
                delta += 1
                down_cnt += 1

            u_cnt = 1
            delta = 1
            while r - delta >= 0 and board[r-delta][c] == up:
                delta += 1
                u_cnt += 1
            delta = 1
            while r + delta < N and board[r+delta][c] == up:
                delta += 1
                u_cnt += 1

            d_cnt = 1
            delta = 1
            while r - delta >= 0 and board[r-delta][c] == down:
                delta += 1
                d_cnt += 1
            delta = 1
            while r + delta < N and board[r+delta][c] == down:
                delta += 1
                d_cnt += 1
            # if max(left_cnt, right_cnt, u_cnt, d_cnt) == 4:
            #     print(r, c)
            ans = max(ans, left_cnt, right_cnt, u_cnt, d_cnt)
print(ans)
