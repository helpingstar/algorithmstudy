import sys
from collections import deque

input = sys.stdin.readline

dist = [0] * 100001
trace = [0] * 100001


def path(x):
    route = deque()
    route.appendleft(x)
    for _ in range(dist[x]-1):
        route.appendleft(trace[route[0]])
    print(*route)


def solution():
    start, end = map(int, input().split())

    if start == end:
        print(0)
        print(start)
        return

    q = deque()
    q.append(start)
    dist[start] = 1

    while q:
        now = q.popleft()

        for nxt in [now + 1, now - 1, now * 2]:
            if 0 <= nxt <= 100000 and dist[nxt] == 0:
                dist[nxt] = dist[now] + 1
                trace[nxt] = now
                if nxt == end:
                    print(dist[now])
                    path(end)
                    return

                q.append(nxt)


solution()
