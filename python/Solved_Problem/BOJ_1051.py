import sys

input = sys.stdin.readline

R, C = map(int, input().split())
board = [input().rstrip() for _ in range(R)]

def check_size(size):
    for r in range(R-size+1):
        for c in range(C-size+1):
            if board[r][c] == board[r+size-1][c] == board[r][c+size-1] == board[r+size-1][c+size-1]:
                return True
    return False

def solution():
    if min(R, C) == 1:
        return 1
    answer = 1
    n_min = min(R, C) + 1
    for size in range(2, n_min+1):
        if check_size(size):
            answer = size * size
            continue
    return answer

print(solution())
