import sys
from collections import deque

input = sys.stdin.readline

dist = [[-1] * 1001 for _ in range(1001)]
dist[1][0] = 0


def solution():
    target = int(input())

    q = deque()
    q.append((1, 0))

    while q:
        now, clip = q.popleft()
        # print(now, clip, dist[now][clip])
        if now + clip == target or now - 1 == target:
            return dist[now][clip] + 1

        if now > 1 and dist[now-1][clip] == -1:
            q.append((now-1, clip))
            dist[now-1][clip] = dist[now][clip] + 1

        if dist[now][now] == -1:
            q.append((now, now))
            dist[now][now] = dist[now][clip] + 1

        if now + clip <= 1000 and dist[now+clip][clip] == -1:
            q.append((now + clip, clip))
            dist[now+clip][clip] = dist[now][clip] + 1


print(solution())
