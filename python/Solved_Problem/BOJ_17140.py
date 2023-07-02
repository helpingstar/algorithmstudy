import sys

input = sys.stdin.readline


def cal_r(board):
    br, bc = len(board), len(board[0])
    new_dic_list = []
    l_max = 0
    for r in range(br):
        n_dic = dict()
        for c in range(bc):
            if board[r][c] == 0:
                continue
            if board[r][c] not in n_dic:
                n_dic[board[r][c]] = 1
            else:
                n_dic[board[r][c]] += 1
        new_dic_list.append(n_dic)
        l_max = max(l_max, len(n_dic))
    l_max = min(50, l_max)
    new_board = [[0] * (l_max*2) for _ in range(br)]
    
    for r in range(br):
        now_dic = new_dic_list[r]
        for i, (k, v) in enumerate(sorted(now_dic.items(), key=lambda x: (x[1], x[0]))):
            if i == 50:
                break
            new_board[r][i*2] = k
            new_board[r][i*2+1] = v
    return new_board

def cal_l(board):
    br, bc = len(board), len(board[0])
    new_dic_list = []
    l_max = 0
    for c in range(bc):
        n_dic = dict()
        for r in range(br):
            if board[r][c] == 0:
                continue
            if board[r][c] not in n_dic:
                n_dic[board[r][c]] = 1
            else:
                n_dic[board[r][c]] += 1
        new_dic_list.append(n_dic)
        l_max = max(l_max, len(n_dic))
    l_max = min(50, l_max)
    new_board = [[0] * bc for _ in range(l_max * 2)]
    
    for c in range(bc):
        now_dic = new_dic_list[c]
        for i, (k, v) in enumerate(sorted(now_dic.items(), key=lambda x: (x[1], x[0]))):
            if i == 50:
                break
            new_board[i*2][c] = k
            new_board[i*2+1][c] = v
    return new_board

def solution():
    r, c, k = map(int, input().split())
    r -= 1
    c -= 1
    board = [list(map(int, input().split())) for _ in range(3)]
    if len(board) > r and len(board[0]) > c and board[r][c] == k:
        return 0
    
    for i in range(1, 101):
        if len(board) >= len(board[0]):
            board = cal_r(board)
        else:
            board = cal_l(board)
        # print(f'[debug] (n_row, n_col) : {len(board), len(board[0])}')
        if len(board) > r and len(board[0]) > c and board[r][c] == k:
            return i
        
    return -1
        
        
print(solution())