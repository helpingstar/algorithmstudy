import sys
import heapq

input = sys.stdin.readline
INF = 1000000

a_pos, b_pos = map(int, input().split())
distance = [INF] * 100001
distance[a_pos] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)

        if now == b_pos:
            return dist

        if distance[now] < dist:
            continue

        if now-1 >= 0 and distance[now-1] > dist+1:
            heapq.heappush(q, (dist+1, now-1))
            distance[now-1] = dist+1
        if now+1 <= 100000 and distance[now+1] > dist+1:
            heapq.heappush(q, (dist+1, now+1))
            distance[now+1] = dist+1
        if now*2 <= 100000 and distance[now*2] > dist:
            heapq.heappush(q, (dist, now*2))
            distance[now*2] = dist

print(dijkstra(a_pos))
