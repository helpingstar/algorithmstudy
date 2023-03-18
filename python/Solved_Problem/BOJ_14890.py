import sys

input = sys.stdin.readline

N, n_step = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

def check_line(line):
    used = [False] * N
    for i in range(N-1):
        if line[i] != line[i+1]:
            if abs(line[i] - line[i+1]) > 1:
                return False

            if line[i] < line[i+1]: # /
                for s in range(n_step):
                    if i-s < 0 or line[i] != line[i-s] or used[i-s]:
                        return False
                    used[i-s] = True

            if line[i] > line[i+1]: # \
                for s in range(n_step):
                    if i+1+s >= N or line[i+1+s] != line[i+1] or used[i+1+s]:
                        return False
                    used[i+1+s] = True
    return True

ans = 0
for r in range(N):
    if check_line(board[r]):
        # print(f'[debug]  r: {r}')
        ans += 1

for c in range(N):
    temp = [board[i][c] for i in range(N)]
    if check_line(temp):
        # print(f'[debug] line = {temp},  c: {c}')
        ans += 1
print(ans)
