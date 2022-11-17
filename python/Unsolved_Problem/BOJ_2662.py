import sys
import copy

input = sys.stdin.readline

money, n_corp = map(int, input().split())

profit = [[0] * (n_corp + 1)]
board = [[0] * (n_corp + 1)]

for _ in range(money):
    temp = list(map(int, input().split()))
    temp[0] = 0
    profit.append(temp)
    board.append([0] * (n_corp+1))

trace = [[0 for _ in range(n_corp+1)] for _ in range(money + 1)]

for c in range(1, n_corp+1):
    new_trace = [[0 for _ in range(n_corp+1)] for _ in range(money + 1)]
    for r in range(1, money+1):
        n_max = -1
        idx = -1
        for i in range(r+1):
            temp = board[i][c-1] + profit[r-i][c]
            if n_max < temp:
                n_max = temp
                idx = r-i

        board[r][c] = n_max
        new_trace[r] = trace[r-idx][:]
        new_trace[r][c] = idx

    trace = new_trace

print(board[money][n_corp])
print(*new_trace[-1][1:])
