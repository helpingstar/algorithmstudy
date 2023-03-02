import sys

input = sys.stdin.readline

R, C = map(int, input().split())

walls = list(map(int, input().split()))
top = 0
top_idx = 0
for i, wall in enumerate(walls):
    if top < wall:
        top_idx = i
        top = wall
answer = 0
left_top = 0
for i in range(top_idx):
    if walls[i] > left_top:
        left_top = walls[i]
    else:
        answer += left_top - walls[i]

right_top = 0
for i in range(C-1, top_idx, -1):
    if walls[i] > right_top:
        right_top = walls[i]
    else:
        answer += right_top - walls[i]

print(answer)
