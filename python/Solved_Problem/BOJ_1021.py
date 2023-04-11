import sys
import copy
from collections import deque

input = sys.stdin.readline


def solution():
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    visited = set()
    visited.add(tuple(i for i in range(1, N+1)))

    q = deque()
    q.append((deque([i for i in range(1, N+1)]), 0, 0))

    while q:
        now, step, cnt = q.popleft()
        # print(now)
        if now[0] == nums[cnt]:
            now.popleft()

            if cnt+1 == M:
                return step
            visited.add(tuple(now))
            q.append((now, step, cnt + 1))
        else:
            left = copy.deepcopy(now)
            left.append(left.popleft())

            if tuple(left) not in visited:
                visited.add(tuple(left))
                q.append((left, step+1, cnt))

            now.appendleft(now.pop())

            if tuple(now) not in visited:
                visited.add(tuple(now))
                q.append((now, step+1, cnt))

print(solution())
