import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())
scores = [0] + list(map(int, input().split()))
score_board = [[0, scores[i]] for i in range(n+1)]
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(now):
    visited[now] = True
    for i in graph[now]:
        if not visited[i]:
            dfs(i)
            score_board[now][1] += score_board[i][0] # now -> 우수 마을로 선정
            score_board[now][0] += max(score_board[i][0], score_board[i][1]) # now -> 우수마을X 

dfs(1)

print(max(score_board[1]))