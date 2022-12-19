import sys
import heapq
input = sys.stdin.readline

n_planet, n_link = map(int, input().split())
position_list = [[-1, -1]]
parent = [i for i in range(n_planet+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def get_dist(a, b):
    dist = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5
    return dist

for _ in range(n_planet):
    a, b = map(int, input().split())
    position_list.append((a, b))

for _ in range(n_link):
    a, b = map(int, input().split())
    union(parent, a, b)

edges = []

for i in range(1, n_planet):
    for j in range(i+1, n_planet+1):
        if find(parent, i) == find(parent, j):
            continue
        heapq.heappush(edges, (get_dist(position_list[i], position_list[j]), i, j))

result = 0
count = n_planet - n_link - 1

while edges:
    cost, a, b = heapq.heappop(edges)
    if find(parent, a) == find(parent, b):
        continue
    # print(f'[debug] edges: {edges}')
    # print(f'[debug]  cost:{cost} a: {a}, b: {b}')
    result += cost
    union(parent, a, b)

print(f'{result:.2f}')
