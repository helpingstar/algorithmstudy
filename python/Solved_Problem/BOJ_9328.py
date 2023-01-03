import sys
from collections import deque, defaultdict
input = sys.stdin.readline

T = int(input())

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

def solution():
    n_row, n_col = map(int, input().split())

    board = [input().rstrip() for _ in range(n_row)]

    key_list = list(input().rstrip())

    if key_list[0] == '0':
        key_list = set()
    else:
        key_list = set(key_list)

    visited = [[False] * n_col for _ in range(n_row)]
    door_dic = defaultdict(set)
    q = deque()

    result = 0

    for r in [0, n_row-1]:
        for c in range(n_col):
            if board[r][c] == '*':
                continue
            elif board[r][c] == '.':
                q.append((r, c))
                visited[r][c] = True
            elif board[r][c] == '$':
                q.append((r, c))
                visited[r][c] = True
                result += 1
            # key : lower
            elif board[r][c].islower():
                q.append((r, c))
                visited[r][c] = True
                # in door dic
                for nr, nc in door_dic[board[r][c].upper()]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

                    door_dic[board[r][c].upper()].remove((nr, nc))
                key_list.add(board[r][c])
            # door
            else:
                if board[r][c].lower() in key_list:
                    q.append((r, c))
                    visited[r][c] = True
                else:
                    door_dic[board[r][c]].add((r, c))

    for r in range(1, n_row-1):
        for c in [0, n_col-1]:
            if board[r][c] == '*':
                continue
            elif board[r][c] == '.':
                q.append((r, c))
                visited[r][c] = True
            elif board[r][c] == '$':
                q.append((r, c))
                visited[r][c] = True
                result += 1
            # key : lower
            elif board[r][c].islower():
                q.append((r, c))
                visited[r][c] = True
                # in door dic
                for nr, nc in door_dic[board[r][c].upper()]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

                    door_dic[board[r][c].upper()].remove((nr, nc))
                key_list.add(board[r][c])
            # door
            else:
                if board[r][c].lower() in key_list:
                    q.append((r, c))
                    visited[r][c] = True
                else:
                    door_dic[board[r][c]].add((r, c))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if not (0 <= nr < n_row and 0 <= nc < n_col):
                continue
            if visited[nr][nc]:
                continue
            if board[nr][nc] == '*':
                continue
            elif board[nr][nc] == '.':
                q.append((nr, nc))
                visited[nr][nc] = True
            elif board[nr][nc] == '$':
                q.append((nr, nc))
                visited[nr][nc] = True
                result += 1
            # key : lower
            elif board[nr][nc].islower():
                q.append((nr, nc))
                visited[nr][nc] = True
                # in door dic
                for dr, dc in door_dic[board[nr][nc].upper()]:
                    visited[dr][dc] = True
                    q.append((dr, dc))

                door_dic[board[nr][nc].upper()] = set()
                key_list.add(board[nr][nc])
            # door
            else:
                if board[nr][nc].lower() in key_list:
                    q.append((nr, nc))
                    visited[nr][nc] = True
                else:
                    door_dic[board[nr][nc]].add((nr, nc))
    return result



for _ in range(T):
    print(solution())
