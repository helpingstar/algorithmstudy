import sys
from collections import deque
input = sys.stdin.readline

def solution():
    a, b = map(int, input().split())
    board = dict()
    q = deque()
    q.append(a)
    board[a] = 0
    while q:
        now = q.popleft()
        if now*2 == b:
            return board[now] + 2
        elif now * 2 < b:
            if now*2 not in board:
                board[now*2] = board[now] + 1
                q.append(now*2)
            else:
                if board[now] + 1 < board[now*2]:
                    board[now*2] = board[now] + 1
                    q.append(now*2)

        if now*10 + 1 == b:
            return board[now] + 2
        elif now * 10 + 1 < b:
            if now * 10 + 1 not in board:
                board[now*10 + 1] = board[now] + 1
                q.append(now*10 + 1)
            else:
                if board[now] + 1 < board[now*10+1]:
                    board[now*10 + 1] = board[now] + 1
                    q.append(now*10 + 1)
    return -1

print(solution())
