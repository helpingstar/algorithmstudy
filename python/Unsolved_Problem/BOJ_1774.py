import sys

input = sys.stdin.readline

# 크루스칼 알고리즘 채택 근거
# 가중치가 있는 무향 그래프의 최소 연결방법
# 아무거나로 시작하지 않아도 되기 때문에, 무향이기 때문에 다익스트라 배제

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# cost가 주어지지 않기 때문에 cost를 얻는 함수를 만든다.
def get_distance(x, y):
    return ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2) ** 0.5

n, m = map(int, input().split())

parent = [i for i in range(n+1)]
result = 0

edges = []
pos = [()]

# position이 하나씩 추가되고 새로 추가되는 pos는 
# 이미 만들어진 pos과의 관계 그래프를 edges에 추가

for i in range(1, n+1):
    x, y = map(int, input().split())
    for j in range(1, len(pos)):
        edges.append((get_distance((x, y), pos[j]), i, j))
    pos.append((x, y))

edges.sort()

# 이미 있는 도로는 연결되고 전체 cost에 추가되지 않기 때문에
# union연산만 수행한다.
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += get_distance(pos[a], pos[b])

print(f'{result:.2f}')