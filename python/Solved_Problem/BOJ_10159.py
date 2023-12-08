import sys

input = sys.stdin.readline

def solution():
    n_good = int(input())
    n_conn = int(input())

    graph = [[[] for _ in range(n_good+1)] for _ in range(2)]

    for _ in range(n_conn):
        a, b = map(int, input().split())
        graph[0][a].append(b)
        graph[1][b].append(a)
    
    visited = [[0, 0] for _ in range(n_good+1)]

    def dfs(now, way, root):
        count = 1
        visited[now][way] = root
        for nxt in graph[way][now]:
            if visited[nxt][way] == root:
                continue
            count += dfs(nxt, way, root)
        return count


    for i in range(1, n_good+1):
        result = 0
        for w in range(2):
            result += dfs(i, w, i)
        print(n_good - result + 1)

solution()