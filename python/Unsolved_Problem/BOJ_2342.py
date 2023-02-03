import sys
from collections import deque, defaultdict
input = sys.stdin.readline
INF = 1e10

def ia(x, y):
    return (min(x, y), max(x, y))

def step(a, b):
    if a == 0:
        return 2
    elif abs(a-b) == 2:
        return 4
    elif a == b:
        return 1
    else:
        return 3

def solution():
    steps = list(map(int, input().split()))
    n_step = len(steps) - 1
    trace = [defaultdict(lambda: INF) for _ in range(n_step)]

    q = deque()
    q.append((0, steps[0], 0))
    trace[0][(0, steps[0])] = 2
    while q:
        x, y, cnt = q.popleft()
        # print(f'[debug]  {x, y, cnt}')
        nextep = steps[cnt+1]
        now_step = trace[cnt][ia(x, y)]
        if x != nextep and cnt < n_step-1 and trace[cnt+1][ia(x, nextep)] >= now_step + step(y, nextep): # change y
            if trace[cnt+1][ia(x, nextep)] == INF:
                q.append((*ia(x, nextep), cnt+1))
            trace[cnt+1][ia(x, nextep)] = now_step + step(x, nextep)
        if y != nextep and cnt < n_step-1 and trace[cnt+1][ia(nextep, y)] >= now_step + step(y, nextep):
            if trace[cnt+1][ia(nextep, y)] == INF:
                q.append((*ia(nextep, y), cnt+1))
            trace[cnt+1][ia(nextep, y)] = now_step + step(nextep, y)
    # print(trace)
    return min(trace[n_step-1].values())

print(solution())
