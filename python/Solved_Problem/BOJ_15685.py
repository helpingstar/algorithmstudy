import sys
from collections import deque, defaultdict

input = sys.stdin.readline

all_point = set()
delta = ((1, 0), (0, -1), (-1, 0), (0, 1))

def next_way(dx, dy):
    if (dx, dy) == (0, 1):      # down
        return (-1, 0)              # left
    elif (dx, dy) == (1, 0):    # right
        return (0, 1)               # down
    elif (dx, dy) == (-1, 0):   # left
        return (0, -1)              # up
    else:                       # up
        return (1, 0)               # right

def dxagon_curve(x, y, s, g):
    global all_point

    dx, dy = delta[s]
    nx, ny = x + dx, y + dy
    all_point.add((x, y))
    all_point.add((nx, ny))
    if g == 0:
        return

    q = deque([(nx, ny), (x, y)])

    # print(f'[debug] q: {q}')

    for j in range(g):
        nq = deque([(q[0][0], q[0][1])])
        for i in range(len(q)-1):
            x1, y1 = q[i]
            x2, y2 = q[i+1]
            dx, dy = next_way(x2-x1, y2-y1)
            # print(f'[debug] (x2-x1, y2-y1) : {x2-x1, y2-y1}, (dx, dy) : {dx, dy}')

            nx, ny = nq[0][0] + dx, nq[0][1] + dy
            # print(f'[debug] (nq[0][0], nq[0][1]) : {nq[0][0], nq[0][1]}')
            # print(f'[debug] (j, i, nx, ny) : {j, i, nx, ny}')
            all_point.add((nx, ny))
            nq.appendleft((nx, ny))
        nq.pop()
        q = nq + q

for _ in range(int(input())):
    x, y, s, g = map(int, input().split())
    dxagon_curve(x, y, s, g)

square = defaultdict(int)
for x, y in all_point:
    square[(x, y)] += 1
    square[(x+1, y)] += 1
    square[(x, y+1)] += 1
    square[(x+1, y+1)] += 1
ans = 0
for v in square.values():
    if v >= 4:
        ans += 1

print(ans)
