from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().rstrip().split())

# 전체 수가 몇개인지 중복을 제거하고 파악한다.
# 중복된 vertex인지 파악하기 위한 딕셔너리를 만들기 위함
num_list = set()

node = {}

# node를 파악하기
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    # a, b가 기존에 없을경우 리스트를 만든다 -> defaultdict 를 썼어야 했다.
    if a not in node.keys():
        node[a] = []
        num_list.add(a) 
    if b not in node.keys():
        node[b] = []
        num_list.add(b)
    if b in node[a]:
        continue
    
    node[a].append(b)
    node[b].append(a)

# 멍청하게 heapq는 sort 상태를 유지해주는 것인줄 알았음 > 아님
# 각 딕셔너리의 요소들을 정렬한다.
for i in num_list:
    node[i].sort()
    
# 아쉬운 코드이긴 함, 더 일반화하고싶음
if v not in num_list:
    print(v)
    print(v)
else:
    bfs_entered_vertex = {}
    for i in num_list:
        bfs_entered_vertex[i] = False

    bfs_print = []

    def bfs(v):
        queue = deque()
        queue.append(v)
        while queue:
            t = queue.popleft()
            if bfs_entered_vertex[t]:
                continue
            bfs_entered_vertex[t] = True
            bfs_print.append(t)

            for i in node[t]:
                queue.append(i)

    dfs_entered_vertex = {}
    for i in num_list:
        dfs_entered_vertex[i] = False
    dfs_print = []

    def dfs(v):
        if dfs_entered_vertex[v]:
            return False
        dfs_entered_vertex[v] = True
        dfs_print.append(v)
        for i in node[v]:
            dfs(i)

    bfs(v)
    dfs(v)

    print(*dfs_print)
    print(*bfs_print)