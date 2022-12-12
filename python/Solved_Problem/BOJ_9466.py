import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def solution():
    n_student = int(input())
    choice_list = list(map(int, input().split()))
    indegree = [0] * (n_student+1)
    graph = defaultdict(list)
    for i, choiced in enumerate(choice_list):
        graph[i+1].append(choiced)
        indegree[choiced] += 1
    ans = 0
    q = deque()

    for i in range(1, n_student+1):
        if indegree[i] == 0:
            q.append(i)
            ans += 1

    # print(f'[debug]  indegree: {indegree}')


    while q:
        now = q.popleft()
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
                ans += 1
    print(ans)




t = int(input())

for _ in range(t):
    solution()
