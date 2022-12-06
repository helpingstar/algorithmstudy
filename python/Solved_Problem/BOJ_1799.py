import sys

input = sys.stdin.readline

N = int(input())

board = []
black = []
white = []
for r in range(N):
    line = list(map(int, input().split()))
    board.append(line)
    for c in range(N):
        if line[c] == 1:
            if (r + c) % 2 == 0:
                black.append((r, c))
            else:
                white.append((r, c))

black_white_max = [0, 0]

right_top = [False] * (2*N + 1)
right_down = [False] * (2*N + 1)

def check(color, index, count, color_index):
    if index == len(color):
        black_white_max[color_index] = max(black_white_max[color_index], count)
        return
    x, y = color[index]

    if right_top[x+y] or right_down[x-y+N-1]:
        check(color, index+1, count, color_index)
    else:
        check(color, index+1, count, color_index)
        right_top[x+y] = True
        right_down[x-y+N-1] = True
        check(color, index+1, count+1, color_index)
        right_top[x+y] = False
        right_down[x-y+N-1] = False

check(black, 0, 0, 0)
check(white, 0, 0, 1)

print(sum(black_white_max))
