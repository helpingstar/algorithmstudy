import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

INF = sys.maxsize

def dfs(city_list):
    start = city_list[0]
    q = deque()
    visited = set()

    q.append(start)
    visited.add(start)
    population = 0
    while q:
        now = q.popleft()
        population += populations[now]
        for next in graph[now]:
            if next in visited:
                continue
            if next not in city_list:
                continue
            q.append(next)
            visited.add(next)
    return population, len(visited)

n_city = int(input())
populations = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n_city+1)]
n_min = INF

for i in range(1, n_city+1):
    temp = list(map(int, input().split()))
    graph[i] += temp[1:]

for n_a in range(1, n_city//2 + 1):
    for a_city in combinations(1, range(n_city+1), n_a):
        a_population, n_a_city = dfs(a_city)
        b_population, n_b_city  = dfs([i for i in range(1, n_city+1) if i not in a_city])
        if n_a_city + n_b_city == n_city:
            n_min = min(n_min, abs(a_population - b_population))

if n_min != INF:
    print(n_min)
else:
    print(-1)
