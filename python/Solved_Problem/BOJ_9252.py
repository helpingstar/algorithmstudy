import sys

input = sys.stdin.readline

def solution():
    s2 = input().rstrip()
    s1 = input().rstrip()
    s1 = ' ' + s1
    s2 = ' ' + s2
    board = [['' for _ in range(len(s2))] for _ in range(len(s1))]
    for r in range(1, len(s1)):
        for c in range(1, len(s2)):
            if s1[r] == s2[c]:
                if (len(board[r-1][c-1]) + 1 >= max(len(board[r-1][c]), len(board[r][c-1]))):
                    board[r][c] = board[r-1][c-1] + s1[r]
                else:
                    board[r][c] = max(board[r-1][c], board[r][c-1], key=len)
            else:
                board[r][c] = max(board[r-1][c], board[r][c-1], key=len)
    return len(board[len(s1)-1][len(s2)-1]), board[len(s1)-1][len(s2)-1]

print(*solution(), sep='\n')
