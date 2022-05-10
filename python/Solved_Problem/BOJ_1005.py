import sys
from collections import deque
input = sys.stdin.readline

# t : test case
t = int(input())
for _ in range(t):
    # n : 빌딩의 개수, k : 규칙의 총 개수
    n, k = map(int, input().split())
    # building time
    time = [0] + list(map(int ,input().split()))
    
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)
    
    max_board = [0] * (n+1)
    
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1
    
    q = deque()
    
    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
            max_board[i] = time[i]
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            max_board[i] = max(max_board[i], max_board[now] + time[i])
            degree[i] -= 1
            if degree[i] == 0:
                q.append(i)
    
    print(max_board[int(input())])