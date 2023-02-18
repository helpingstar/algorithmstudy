import sys

input = sys.stdin.readline

n = int(input())

board = [input().rstrip() for _ in range(n)]

def dp(x, y, size):
    # if size == 2:
    #     ans = ''
    #     ans += board[x][y:y+2]
    #     ans += board[x+1][y:y+2]
    #     return '(' + ans + ')'
    
    cr = board[x][y]
    
    # print(f'[debug] x, y, size: {x, y, size}')
    all_same = True
    for r in range(size):
        # print(f'[debug] a : {board[x+r][y:y+size]}')
        # print(f'[debug] b : {cr*size}')
        if board[x+r][y:y+size] != cr*size:
            all_same = False
            break
        
    if all_same:
        return cr
    else:
        new_size = size // 2
        return ('(' 
                + dp(x, y, new_size) 
                + dp(x, y+new_size, new_size) 
                + dp(x + new_size, y, new_size) 
                + dp(x + new_size, y + new_size, new_size) 
                + ')')

print(dp(0, 0, n))