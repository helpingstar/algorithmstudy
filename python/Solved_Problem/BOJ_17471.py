import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline


def solution():
    N = int(input())
    populations = [0] + list(map(int, input().split()))
    t_populations = sum(populations)
    graph = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        graph[i] = list(map(int, input().split()))[1:]
    all_combinations = []
    for i in range(1,  N // 2 + 1):
        for comb in combinations(range(1, N+1), i):
            team1_score = 0
            for i in comb:
                team1_score += populations[i]
            team2_score = t_populations - team1_score

            all_combinations.append((abs(team1_score-team2_score), comb))
    all_combinations.sort()

    for diff, comb in all_combinations:
        cnt = 1
        start1 = comb[0]
        for i in range(1, N+1):
            if i not in comb:
                start2 = i
                break
        visited = [False] * (N+1)
        visited[start1] = True
        q = deque([start1])
        while q:
            now = q.popleft()
            for next_ in graph[now]:
                if next_ not in comb:
                    continue
                if visited[next_]:
                    continue
                q.append(next_)
                visited[next_] = True
                cnt += 1
        if cnt != len(comb):
            continue
        visited[start2] = True
        q = deque([start2])
        cnt += 1
        while q:
            now = q.popleft()
            for next_ in graph[now]:
                if next_ in comb:
                    continue
                if visited[next_]:
                    continue
                q.append(next_)
                visited[next_] = True
                cnt += 1
        if cnt == N:
            return diff
    return -1


print(solution())
