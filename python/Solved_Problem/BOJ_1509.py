import sys

input = sys.stdin.readline

word = input().rstrip()

L = len(word)

board = [[0] * L for _ in range(L)]

for size in range(L):
    for start in range(L-size):
        end = start + size
        if size == 0:
            board[start][end] = 1
        elif size == 1:
            if word[start] == word[end]:
                board[start][end] = 1
        else:
            if board[start+1][end-1] == 1:
                if word[start] == word[end]:
                    board[start][end] = 1

dp = [2600] * (L+1)
dp[0] = 0

for i in range(L):
    for j in range(i, L):
        if board[i][j] == 1:
            dp[j+1] = min(dp[j+1], dp[i] + 1)
print(dp[-1])