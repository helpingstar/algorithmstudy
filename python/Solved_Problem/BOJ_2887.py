import sys

input = sys.stdin.readline

n = int(input())

position_list = []

for i in range(n):
    a, b, c = map(int, input().split())
    position_list.append((a, b, c, i+1))

edges = []

for i in range(3):
    position_list.sort(key=lambda x: x[i])
    for j in range(n-1):
        edges.append((abs(position_list[j][i] - position_list[j+1][i]), position_list[j][3], position_list[j+1][3]))

edges.sort()

parent = [i for i in range(n+1)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

count = 0
ans = 0
for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        # print(f'[debug] cost: {cost}, a:{a}, b:{b}')
        union_parent(parent, a, b)
        count += 1
        ans += cost

    # if count == n-1:
    #     break;

print(ans)
