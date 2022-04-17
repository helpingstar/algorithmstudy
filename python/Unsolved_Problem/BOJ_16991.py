import sys

input = sys.stdin.readline

n = int(input())
graph = [[0] * n for _ in range(n)]
pos = []
for i in range(n):
    pos.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1, n):
        x_i, y_i = pos[i]
        x_j, y_j = pos[j]
        graph[i][j] = graph[j][i] = ((x_i-x_j) ** 2 + (y_i-y_j) ** 2) ** 0.5

INF = 1e9
# 공간복잡도는 O(n(2^n))이므로 n X (n2^n)이 아니라 n X (2*n) 이 맞다.
dp = [[INF] * (1 << n) for _ in range(n)]

def dfs(x, visited):
    # 모든 장소를 방문하면
    if visited == (1 << n) - 1:
        # graph 가 존재하면 길이 있다는 것이니까 graph를 리턴한다.
        # 요소로써 INF는 dp와 관계있지 graph와 관계 없다.
        if graph[x][0]:
            return graph[x][0]
        # 돌아가는 길이 없다면 INF를 반환한다.
        else:
            return INF
    
    # 이미 값이 있다면
    if dp[x][visited] != INF:
        return dp[x][visited]


    for i in range(1, n):
        # 이 두 조건을 놓쳤다.
        # 가는 길이 없다면 continue
        if not graph[x][i]:
            continue
        # 이미 방문했다면 continue
        if visited & (1 << i):
            continue
        dp[x][visited] = min(dp[x][visited], graph[x][i] + dfs(i, visited | (1 << i)))
    
    return dp[x][visited]

print(dfs(0, 1))