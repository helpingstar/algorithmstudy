import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

move = {}
start_set = set()

for _ in range(n + m):
    a, b = map(int, sys.stdin.readline().split())
    move[a] = b
    start_set.add(a)

game_table = [101] * 101
game_table[1] = 0

queue = deque()
queue.append(1)
while queue:
    t = queue.popleft()
    for i in range(1, 7):
        nx = t + i
        if not (1 < nx <= 100):
            continue
        if nx in start_set:
            if game_table[t] + 1 >= game_table[move[nx]]:
                continue
            game_table[move[nx]] = game_table[t] + 1
            queue.append(move[nx])
        else:
            if game_table[t] + 1 >= game_table[nx]:
                continue
            game_table[nx] = game_table[t] + 1
            queue.append(nx)
    if game_table[100] != 101:
        break

print(game_table[100])