import sys

input = sys.stdin.readline

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

n = int(input())

parent = [0] * (n+1)
edges = []
result = 0
position = []

for i in range(n):
    parent[i] = i

'''
여기서 메모리 초과가 났다. (n^2)
for i in range(n):
    x, y, z = map(int, input().split())
    for j in range(i):
        edges.append((min(abs(position[j][0] - x), abs(position[j][1]-y), abs(position[j][2]-z)), i, j))
    position.append([x, y, z])
'''

'''
터널 연결 비용이 min(|xA-xB|, |yA-yB|, |zA-zB|) 라는 것이 핵심이다.
각 좌표를 1차원으로 나열할 경우 (x1 to x3) = (x1 to x2) + (x2 to x3) 이기 때문에
각각을 모두 연결해 줄 수 있는 최소값만 필요하므로 공간복잡도를 3(n-1)까지 줄일 수 있다.
'''
for i in range(n):
    x, y, z = map(int, input().split())
    # 좌표, 인덱스
    position.append((x, y, z, i))

for i in range(3):
    position.sort(key=lambda x:x[i])
    for j in range(1, n):
        # (x[n-1] to x[n], n-1, n)
        edges.append((abs(position[j - 1][i] - position[j][i]), position[j-1][3], position[j][3]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

4
'''