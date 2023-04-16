import sys

input = sys.stdin.readline

V, E, budget = map(int, input().split())

cost = [0] + list(map(int, input().split()))

parent = [i for i in range(V+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, apast, bpast):
    a = find(parent, apast)
    b = find(parent, bpast)

    if cost[a] > cost[b]:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(E):
    a, b = map(int, input().split())
    union(parent, a, b)

ans = 0
for i in range(1, V+1):
    now = find(parent, i)
    if now == i:
        ans += cost[now]
        if budget - ans < 0:
            break

if budget - ans < 0:
    print('Oh no')
else:
    print(ans)
