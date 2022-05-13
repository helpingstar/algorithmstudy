import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for _ in range(m):
    u, v = map(int, input().split())
    union(u, v)

result = set()

for i in range(1, n+1):
    result.add(find(i))

print(len(result))