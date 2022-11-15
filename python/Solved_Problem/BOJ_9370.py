import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

n_testcase = int(input())

INF = sys.maxsize

def solution():
    n_vertex, n_edge, n_candidate = map(int, input().split())
    start, s_road1, s_road2 = map(int, input().split())
    graph = defaultdict(dict)
    for _ in range(n_edge):
        a, b, dist = map(int, input().split())
        graph[a][b] = dist
        graph[b][a] = dist
    candidates = [int(input()) for _ in range(n_candidate)]
    # print(f'[D]  graph : {graph}')

    def dijkstra(start):
        distance = [INF] * (n_vertex + 1)
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for next, new_dist in graph[now].items():
                cost = dist + new_dist
                # print(f'[D]  |now:{now}|next:{next}|dist:{dist}|new_dist:{new_dist}|')
                if cost < distance[next]:
                    heapq.heappush(q, (cost, next))
                    distance[next] = cost
        return distance
    ans = []
    start_distance = dijkstra(start)
    for cand in candidates:
        cand_distance = dijkstra(cand)
        # print(f'[debug]  start_distance : {start}, {start_distance}')
        # print(f'[debug]  cand_distance  : {cand}, {cand_distance}')

        if start_distance[cand] != INF and \
            (start_distance[s_road1] + graph[s_road1][s_road2] + cand_distance[s_road2] == start_distance[cand] or \
            start_distance[s_road2] + graph[s_road2][s_road1] + cand_distance[s_road1] == start_distance[cand]):
                ans.append(cand)
    ans.sort()
    return ans


for _ in range(n_testcase):
    print(*solution())
