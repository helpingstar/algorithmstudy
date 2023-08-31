import sys
import heapq


def solution():
    input = sys.stdin.readline

    N, K = map(int, input().split())

    if N == K:
        return 0

    END = 100001

    dist = [END] * END
    q = [(0, N)]
    dist[N] = 0

    while q:
        step, now = heapq.heappop(q)
        if now == K:
            return dist[K]

        for delta, nxt in ((1, now+1), (1, now-1), (0, now*2)):
            if not (0 <= nxt < END):
                continue
            if dist[now] + delta >= dist[nxt]:
                continue
            dist[nxt] = dist[now] + delta
            heapq.heappush(q, (dist[nxt], nxt))


print(solution())
