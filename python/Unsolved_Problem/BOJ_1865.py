import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    for i in range(n):
        for j in range(m*2 + w):
            cur, next_node, cost = graph[j]
            # distance[cur] != INF 을 없애니까 답이 되었다. 
            # distance[cur] != INF 가 있을경우 시작을 1로 했을때 반례
            # 1
            # 3 2 0
            # 2 3 -1
            # 3 2 -1
            # 즉 첫 "cur"이 INF인 경우 문제를 풀지 못하게 된다.
            # ex) 첫 cur이 INF여서 지나쳤는데 첫 "cur"과 연계된 것들이 고립되었을때 문제를 풀지 못하게 된다.
            # 벨만포드 알고리즘은 어느곳으로 시작해도 사이클 판단이 가능하다.
            if distance[next_node] > distance[cur] + cost:
                distance[next_node] = distance[cur] + cost
                if i == n - 1:
                    return True
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))
    if bf(1):
        print('YES')
    else:
        print('NO')
        
        
import sys

def solution(N, edges):
    g = [100000000 for _ in range(N + 1)]
    g[0] = 0
    for _ in range(N):
        update = False
        for s, e, t in edges:
            if g[e] > g[s] + t:
                g[e] = g[s] + t
                update = True
        
        if not update: break

    for s, e, t in edges:
        if g[e] > g[s] + t:
            return 'YES'

    return 'NO'

if __name__ == '__main__':
    TC = int(sys.stdin.readline())
    for _ in range(TC):
        N, M, W = map(int, sys.stdin.readline().split())
        edges = []
        for _ in range(M):
            s, e, w = map(int, sys.stdin.readline().split())
            edges.append((s, e, w))
            edges.append((e, s, w))
        
        for _ in range(W):
            s, e, w = map(int, sys.stdin.readline().split())
            edges.append((s, e, -w))
        
        sys.stdout.write('%s\n'%solution(N, edges))