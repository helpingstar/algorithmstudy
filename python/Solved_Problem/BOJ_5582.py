import sys

input = sys.stdin.readline

a_string = input().rstrip()
b_string = input().rstrip()

board = [[0] * len(a_string) for _ in range(len(b_string))]
answer = 0

for r in range(len(b_string)):
    for c in range(len(a_string)):
        if b_string[r] == a_string[c]:
            if r == 0 or c == 0:
                board[r][c] = 1
            else:
                board[r][c] = board[r-1][c-1] + 1
            answer = max(answer, board[r][c])

print(answer)
