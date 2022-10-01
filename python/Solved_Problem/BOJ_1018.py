import sys

input = sys.stdin.readline
n, m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]
ans = sys.maxsize
def get_min_num(x:int, y:int)->int:
    first_black = 0
    first_white = 0
    for r in range(x, x+8):
        for c in range(y, y+8):
            if board[r][c] == 'B':
                if (r+c) % 2 == 0:
                    first_white += 1
                else:
                    first_black += 1
            else:
                if (r+c) % 2 == 0:
                    first_black += 1
                else:
                    first_white += 1
    return min(first_black, first_white)

for i in range(n - 7):
    for j in range(m - 7):
        ans = min(ans, get_min_num(i, j))

print(ans)
