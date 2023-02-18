import sys

input = sys.stdin.readline

n_city = int(input())
n_plan = int(input())

graph = [list(map(int, input().split())) for _ in range(n_city)]

plan = list(map(int, input().split()))

parent = [i for i in range(n_city+1)]

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a

for i in range(n_city):
    for j in range(i+1, n_city):
        if graph[i][j]:
            union(parent, i, j)

rep = find(parent, plan[0]-1)

all_same = True

for p in plan[1:]:
    if find(parent, p-1) != rep:
        all_same = False

# print(f'[debug]  rep : {rep}')
# for p in plan:
#     print(f'[debug]  {find(parent, p-1)}')

if all_same:
    print('YES')
else:
    print('NO')