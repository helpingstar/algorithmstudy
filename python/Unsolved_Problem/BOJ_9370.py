# 최단경로가 여러개일 경우 틀릴 수 있다.
# 아직도 왜틀렸는지 모르겠다.

import sys
import heapq
input = sys.stdin.readline

T = int(input())
INF = int(1e10)

# 다익스트라를 한번만 실행한다.
def dijkstra(start, pass1, pass2):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next, new_dist in graph[now]:
            cost = new_dist + dist
            # 경로가 여러개일 수 있기 때문에 미만이 아닌 이하관계로 탐색을 진행한다.
            if cost <= distance[next]:
                distance[next] = cost
                heapq.heappush(q, (cost, next))
                # 현재가 도로를 지나간 상태면 다음것도 지나간 것일 것임
                if check_through[now]:
                    check_through[next] = True
                # 다리에 해당하는 곳을 지나쳤다면 next를 True로 바꾼다.
                elif (pass1, pass2) == (now, next) or (pass1, pass2) == (next, now):
                    check_through[next] = True

for _ in range(T):
    v, e, n_cand = map(int, input().split())
    start, pass1, pass2 = map(int, input().split())
    distance = [INF] * (v+1)
    graph = [[] for _ in range(v+1)]
    # 지나갔는지를 체크하는 리스트
    check_through = [False] * (v+1)

    for _ in range(e):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    cands = []
    for _ in range(n_cand):
        cands.append(int(input()))

    # 다익스트라 호출 부분
    dijkstra(start, pass1, pass2)
    
    cands.sort()
    # 지나쳤다면 cands를 append해서 출력한다.
    ans = []
    for i in cands:
        if check_through[i]:
            ans.append(i)
    print(*ans)