import sys
from collections import deque

input = sys.stdin.readline


def solution():
    # color -> 0: white, 1: red, 2: blue
    # way   -> 0: R,  1: L,  2: U,  3: D
    move = ((0, 1), (0, -1), (-1, 0), (1, 0))
    mirror = ((0, -1), (0, 1), (1, 0), (-1, 0))
    mirror_way = (1, 0, 3, 2)
    n_size, n_mem = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n_size)]
    stack_board = [[deque() for _ in range(n_size)] for _ in range(n_size)]

    mem_list = []
    for i in range(n_mem):
        r, c, way = map(int, input().split())
        mem_list.append([r - 1, c - 1, way - 1])
        stack_board[r-1][c-1].append(i)
    
    def not_valid_pos(r, c):
        return not (0 <= r < n_size and 0 <= c < n_size) or board[r][c] == 2

    def next_pos(r, c, way):
        # candidate
        cr = r + move[way][0]
        cc = c + move[way][1]
        
        if not_valid_pos(cr, cc):
            mcr = r + mirror[way][0]
            mcc = c + mirror[way][1]
            
            if not_valid_pos(mcr, mcc):
                return r, c, 2
            else:
                return mcr, mcc, 1
        else:
            return cr, cc, 0
        
    for i in range(1000):
        for m in range(n_mem):
            mr, mc, mway = mem_list[m]
            nr, nc, is_mirror = next_pos(mr, mc, mway)
            if is_mirror >= 1:
                mem_list[m][2] = mirror_way[mway]
            if is_mirror == 2:
                continue
            ncolor = board[nr][nc]

            mem_stack = deque()
            
            now_deque = stack_board[mr][mc]
            while now_deque and now_deque[-1] != m:
                mem_stack.appendleft(now_deque.pop())
            mem_stack.appendleft(now_deque.pop())

            if ncolor == 0:
                while mem_stack:
                    now = mem_stack.popleft()
                    stack_board[nr][nc].append(now)
                    mem_list[now][0], mem_list[now][1] = nr, nc
            else:
                while mem_stack:
                    now = mem_stack.pop()
                    stack_board[nr][nc].append(now)
                    mem_list[now][0], mem_list[now][1] = nr, nc

            if len(stack_board[nr][nc]) >= 4:
                print(i+1)
                return
    print(-1)

solution()
    