n = int(input())

INF = int(1e9)

# dp[cur][visited]
# 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 돌아가는데 드는 최소 비용
# cur: 현재의 도시, visited: 방문 현황(거쳐간 도시)
dp = [[INF] * (1 << n) for _ in range(n)]


def dfs(x, visited):
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면(visited == 1111)
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    # 여기를 뚫으면 i를 탐색한다(최소값은 보장하지 않음)
    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            print(x, i)
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip
            continue
        # min(현상 유지 vs i를 방문하고 x(출발) -> i(탐색) 의 weight를 더한값)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))