import sys
from collections import deque
input = sys.stdin.readline

visited = set()

rome = (1, 5, 10, 50)

N = int(input())

q = deque()
q.append((0, 0))
visited.add((0, 0))
target_count = 0

while q:
    now, count = q.popleft()
    for num in rome:
        if (now+num, count+1) not in visited and count < N:
            if count+1 == N:
                target_count += 1
            q.append((now+num, count+1))
            visited.add((now+num, count+1))

print(target_count)
