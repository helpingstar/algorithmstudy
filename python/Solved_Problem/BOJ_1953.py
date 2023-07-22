import sys
from collections import deque

input = sys.stdin.readline

def solution():
    N = int(input())
    team = [-1] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        graph[i] = list(map(int, input().split()))[1:]

    q = deque()

    for i in range(1, N + 1):
        if team[i] != -1:
            continue
        q.append((i, 1))
        while q:
            human, t = q.popleft()
            team[human] = t
            next_t = 2 if t == 1 else 1
            for next_human in graph[human]:
                if team[next_human] != -1:
                    continue
                q.append((next_human, next_t))

    team1 = []
    team2 = []
    for i in range(1, N + 1):
        if team[i] == 1:
            team1.append(i)
        else:
            team2.append(i)

    print(len(team1))
    print(*team1)
    print(len(team2))
    print(*team2)

solution()
