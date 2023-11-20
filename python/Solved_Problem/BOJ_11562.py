import sys

input = sys.stdin.readline

def solution():
    n_building, n_road = map(int, input().split())
    dist = [[n_building] * (n_building+1) for _ in range(n_building+1)]
    for _ in range(n_road):
        a, b, w = map(int, input().split())
        if w == 0:
            dist[a][b] = 0
            dist[b][a] = 1
        else:
            dist[a][b] = 0
            dist[b][a] = 0

    for i in range(1, n_building+1):
        dist[i][i] = 0

    for k in range(1, n_building+1):
        for i in range(1, n_building+1):
            for j in range(1, n_building+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    n_question = int(input())
    for _ in range(n_question):
        a, b = map(int, input().split())
        print(dist[a][b])

solution()
