import sys

input = sys.stdin.readline

n_city, n_cable, n_plant = map(int, input().split())
plants = list(map(int, input().split()))

edges = []
for _ in range(n_cable):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

parent = [i for i in range(n_city+1)]
for plant in plants:
    parent[plant] = 0

def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

ans = 0

def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for c, a, b in edges:
    p_a = find_parent(a, parent)
    p_b = find_parent(b, parent)
    if p_a != p_b:
        union_parent(a, b, parent)
        # print(f'[debug]  a:{a}, b:{b}, c:{c}')
        ans += c

print(ans)
