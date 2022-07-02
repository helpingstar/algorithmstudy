import sys
from collections import deque, defaultdict
INF = 1e10

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [defaultdict(int) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = max(graph[a][b], c)
    graph[b][a] = max(graph[b][a], c)

start, end = map(int, input().split())

weight = [0] * (v+1)
weight[start] = INF

"""
다익스트라랑 비슷하다
가능한 값을 들고다니며 weight[now] 보다 작으면 continue한다
bag값이 없을 경우 갔던 곳을 또 가는 문제가 있다. 한곳은 한 bag만 거치게 된다.
"""
def bfs(start):
    # q = []
    # heapq.heappush(q, (-INF, start))
    q = deque()
    q.append((INF, start))
    while q:
        # bag, now = heapq.heappop(q)
        bag, now = q.popleft()
        if bag < weight[now]:
            continue
        for next, bridge in graph[now].items():
            cost = min(bag, bridge)
            if cost > weight[next] and cost > weight[end]:
                weight[next] = cost
                # heapq.heappush(q, (-cost, next))
                if next != end:
                    q.append((cost, next))

bfs(start)

print(weight[end])