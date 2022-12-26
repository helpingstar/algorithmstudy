import sys

input = sys.stdin.readline

n = int(input())

weights = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n+1)]

score = [[0, weights[i]] for i in range(n+1)]
trace = [[set(), {i}] for i in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited = [False] * (n+1)

def dp(now):
    visited[now] = True
    for next in graph[now]:
        if visited[next]:
            continue
        next_dp = dp(next)
        if next_dp[0] > next_dp[1]:
            score[now][0] += next_dp[0]
            trace[now][0] |= trace[next][0]
        else:
            score[now][0] += next_dp[1]
            trace[now][0] |= trace[next][1]
        score[now][1] += dp(next)[0]
        trace[now][1] |= trace[next][0]
    return score[now]

dp(1)

if score[1][0] > score[1][1]:
    print(score[1][0])
    print(*sorted(trace[1][0]))
else:
    print(score[1][1])
    print(*sorted(trace[1][1]))