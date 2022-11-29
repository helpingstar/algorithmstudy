import sys
import heapq

input = sys.stdin.readline

n_region, capacity = map(int, input().split())
n_box = int(input())

mission = [[] for _ in range(n_region+1)]

for _ in range(n_box):
    start, end, box = map(int ,input().split())
    heapq.heappush(mission[end], (-start, box))

now_in_truck = [0] * (n_region+1)
ans = 0

for now in range(n_region, 0, -1):
    ans += now_in_truck[now]
    capacity += now_in_truck[now]
    now_in_truck[now] = 0
    while capacity != 0 and mission[now]:
        start, box = heapq.heappop(mission[now])
        start *= -1
        burden_box = min(capacity, box)
        now_in_truck[start] += burden_box
        capacity -= burden_box
        # print(f'[debug]  now:{now}, end:{end}, box:{box}, capacity:{capacity}, burden_box:{burden_box}')

print(ans)
