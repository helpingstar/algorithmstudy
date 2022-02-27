from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegeree = [0] * (n+1)

for _ in range(m):
    singers = list(map(int, input().split()))
    # 첫 번째 수는 개수를 세는 수이기 때문에 1 index 부터 시작
    for i in range(2, len(singers)):
        graph[singers[i-1]].append(singers[i])
        indegeree[singers[i]] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegeree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegeree[i] -= 1
            if indegeree[i] == 0:
                q.append(i)
    
    # 순환이 있다는 것은 모든 수를 포함하지 못하고 큐가 마무리 된다는 뜻이므로
    # 큐 순환이 끝날 때 노드의 개수와 result 의 개수가 맞지 않다면 이는
    # 그래프 안에 순환이 있다는 뜻이다.
    if len(result) == n:
        return result
    else:
        return [0]

print(*topology_sort(), sep='\n')