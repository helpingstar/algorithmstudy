import sys
from collections import deque
input = sys.stdin.readline


def solution():
    n_store = int(input())
    sx, sy = map(int, input().split())
    stores = []
    for _ in range(n_store):
        cx, cy = map(int, input().split())
        stores.append((cx, cy))
    tx, ty = map(int, input().split())
    stores.append((tx, ty))
    visited = set()
    visited.add((sx, sy))
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        # print(f'[debug]  x, y : {x, y}')
        for nx, ny in stores:
            if (nx, ny) in visited:
                continue
            cost = abs(nx - x) + abs(ny - y)
            if cost <= 1000:
                if nx == tx and ny == ty:
                    return "happy"
                q.append((nx, ny))
                visited.add((nx, ny))
    return "sad"


for _ in range(int(input())):
    print(solution())
