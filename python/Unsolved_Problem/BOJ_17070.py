import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

def solution():
    ans = 0
    q = deque()
    q.append(((0, 1), 0))
    while q:
        (r2, c2), spin = q.popleft()
        if spin == 0:
            if (c2+1 < n) and (board[r2][c2+1] == 0):
                if (r2, c2+1) == (n-1, n-1):
                    ans += 1
                else:
                    q.append(((r2, c2+1), 0))
            else:
                continue
            if (r2+1 < n and board[r2+1][c2] + board[r2+1][c2+1] == 0):
                if (r2+1, c2+1) == (n-1, n-1):
                    ans += 1
                else:
                    q.append(((r2+1, c2+1), 2))
            else:
                continue
        elif spin == 1:
            if (r2+1 < n) and (board[r2+1][c2] == 0):
                if (r2+1, c2) == (n-1, n-1):
                    ans += 1
                else:
                    q.append(((r2+1, c2), 1))
            else:
                continue
            if (c2+1 < n and board[r2][c2+1] + board[r2+1][c2+1] == 0):
                if (r2+1, c2+1) == (n-1, n-1):
                    ans += 1
                else:
                    q.append(((r2+1, c2+1), 2))
            else:
                continue
        else:
            can1 = can2 = False
            if (r2+1 < n) and (board[r2+1][c2] == 0):
                if (r2+1, c2) == (n-1, n-1):
                    ans += 1
                else:
                    q.append(((r2+1, c2), 1))
                can1 = True
            if (c2+1 < n) and (board[r2][c2+1] == 0):
                if (r2, c2+1) == (n-1, n-1):
                    ans += 1
                else:
                    q.append(((r2, c2+1), 0))
                can2 = True
            if (can1 and can2 and board[r2+1][c2+1] == 0):
                if (r2+1, c2+1) == (n-1, n-1):
                    ans += 1
                else:
                    q.append(((r2+1, c2+1), 2))
            else:
                continue
    return ans

print(solution())
