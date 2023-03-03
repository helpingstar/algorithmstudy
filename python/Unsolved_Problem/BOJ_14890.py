import sys

input = sys.stdin.readline

n_size, n_step = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n_size)]


def check_row(row, right_way):
    if right_way:
        search_list = range(n_size)
    else:
        search_list = range(n_size-1, -1, -1)

    cnt = 1
    for i in range(1, n_size):
        # print(row, i)
        if board[row][search_list[i]] == board[row][search_list[i-1]]:
            cnt += 1
        else:
            if board[row][search_list[i]] - board[row][search_list[i-1]] == 1:
                if cnt >= n_step:
                    cnt = 1
                else:
                    return False
            else:
                return False
    return True


def check_col(col, right_way):
    if right_way:
        search_list = range(n_size)
    else:
        search_list = range(n_size-1, -1, -1)

    cnt = 1
    for i in range(1, n_size):
        if board[search_list[i]][col] == board[search_list[i-1]][col]:
            cnt += 1
        else:
            if board[search_list[i]][col] - board[search_list[i-1]][col] == 1:
                if cnt >= n_step:
                    cnt = 1
                else:
                    return False
            else:
                return False
    return True


def check_two_row(row):
    # if check_row(row, True) or check_row(row, False):
        # print(f'[debug] {row}')
    return check_row(row, True) or check_row(row, False)


def check_two_col(col):
    if check_col(col, True) or check_col(col, False):
        print(f'[debug] {col}')
    return check_col(col, True) or check_col(col, False)


result = 0

for r in range(n_size):
    if check_two_row(r):
        result += 1

for c in range(n_size):
    if check_two_col(c):
        result += 1

print(result)
