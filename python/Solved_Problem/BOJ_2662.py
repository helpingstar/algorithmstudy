import sys

input = sys.stdin.readline

n_budget, n_com = map(int, input().split())

profit_table = [[0] * (n_com+1)]
board = [[0] * (n_com+1)]
prev_trace = [[0] * (n_com+1)]
for _ in range(n_budget):
    temp = list(map(int, input().split()))
    temp[0] = 0
    profit_table.append(temp)
    board.append([0] * (n_com+1))
    prev_trace.append([0] * (n_com+1))


for c in range(1, n_com+1):
    trace = [[0] * (n_com+1)]
    for r in range(1, n_budget+1):
        for b in range(0, r+1):
            temp = board[r-b][c-1] + profit_table[b][c]
            if temp > board[r][c]:
                board[r][c] = temp
                select = b
        temp_trace = prev_trace[r-select][:]
        temp_trace[c] = select

        trace.append(temp_trace)
    prev_trace = trace


print(board[n_budget][n_com])
print(*prev_trace[n_budget][1:])
