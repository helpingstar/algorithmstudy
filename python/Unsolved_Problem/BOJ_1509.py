import sys

input = sys.stdin.readline

string = input().rstrip()
length = len(string)

board = [[0] * length for _ in range(length)]

for l in range(length):
    for start in range(length-l):
        end = start + l
        if l == 0:
            board[start][end] = 1
        elif l == 1:
            if string[start] == string[end]:
                board[start][end] = 1
        else:
            if board[start+1][end-1]:
                if string[start] == string[end]:
                    board[start][end] = 1

number = [0] + [3000] * length


for start in range(length):
    for size in range(length-start):
        end = start + size
        # print(start, end)
        if board[start][end] == 1:
            # print(board[start][end])
            number[end+1] = min(number[end+1], number[start] + 1)

print(number[-1])
