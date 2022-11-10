import sys
from collections import deque

input = sys.stdin.readline

dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

first = ''
for _ in range(3):
    temp = ''.join(input().split())
    first += temp

def bfs(first):
    check = set()
    q = deque()
    check.add(first)
    q.append((first, 0))

    while q:
        now, cnt = q.popleft()
        if now == '123456780':
            return cnt
        pos = now.find('0')
        x, y = pos // 3, pos % 3
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            new_pos = nx * 3 + ny

            if not (0 <= nx < 3 and 0 <= ny < 3):
                continue
            now_list = list(now)
            now_list[pos], now_list[new_pos] = now_list[new_pos], now_list[pos]
            new_str = ''.join(now_list)
            if new_str in check:
                continue
            q.append((new_str, cnt+1))
            check.add(new_str)

    return -1


print(bfs(first))
