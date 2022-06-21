# root가 1이 아닐수도 있다는 것을 몰랐다.

import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
have_parent = [False] * (n+1)

for _ in range(n):
    parent, left, right = map(int, input().split())
    graph[parent].append(left)
    graph[parent].append(right)

    if left != -1:
        have_parent[left] = True
    if right != -1:
        have_parent[right] = True


depth = defaultdict(list)

count = 0

# left first search 방식으로 요소가 추가될때마다 depth에 count를 append한다.
def dfs(cnt, root):
    global count
    if graph[root][0] == -1 and graph[root][1] == -1:
        depth[cnt].append(count)
        count += 1
        return
    if graph[root][0] != -1:
        dfs(cnt+1, graph[root][0])
    depth[cnt].append(count)
    count += 1
    if graph[root][1] != -1:
        dfs(cnt+1, graph[root][1])
    return

def find_root():
    for i in range(1, n+1):
        if have_parent[i] == False:
            return i

root = find_root()

dfs(1, root)

ans_depth = 0
ans_length = 0

for i in range(1, len(depth)+1):
    length = max(depth[i]) - min(depth[i]) + 1
    if ans_length < length:
        ans_depth = i
        ans_length = length

print(ans_depth, ans_length)