import sys
import bisect
from collections import deque


def solution():
    INF = int(1e7)
    
    input = sys.stdin.readline
    N, goal = map(int, input().split())
    positions = list(map(int, input().split()))
    steps = list(map(int, input().split()))
    q = deque()
    start_index = 0
    steps_track = [INF] * N
    
    if positions[start_index] + steps[start_index] >= goal:
        return 0
    steps_track[start_index] = 0
    q.append((0, start_index))

    while q:
        step, idx = q.popleft()
        if step > steps_track[idx]:
            continue
        next_idx = bisect.bisect_right(positions, positions[idx] + steps[idx])
        # print(next_idx)
        for i in range(next_idx-1, idx, -1):
            if positions[i] + steps[i] >= goal:
                return step + 1
            if steps_track[i] > step + 1:
                steps_track[i] = step + 1
                q.append((step + 1, i))
    return -1


if __name__ == "__main__":
    print(solution())