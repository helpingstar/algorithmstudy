import sys
from collections import deque
import copy
input = sys.stdin.readline

R, C = map(int, input().split())

def pm(string):
    for r in range(R):
        print(string[r*R: r*R+C])
    print('-------------')

s_map = {'1': '0', '0': '1'}

def solution():
    matrix = ''
    target = ''
    for _ in range(R):
        matrix += input().rstrip()
    for _ in range(R):
        target += input().rstrip()

    visited = set()
    visited.add(matrix)
    q = deque()
    q.append((matrix, 0))
    while q:
        now, step = q.popleft()
        # print(step)
        # pm(now)
        for r in range(R - 2):
            for c in range(C - 2):
                nxt = list(now)
                for i in range(3):
                    for j in range(3):
                        nr = r + i
                        nc = c + j
                        nxt[nr*C+nc] = s_map[nxt[nr*C+nc]]
                nxt_str = ''.join(nxt)
                if nxt_str in visited:
                    continue
                if nxt_str == target:
                    return step + 1
                visited.add(nxt_str)
                q.append((nxt_str, step+1))

    return -1

print(solution())
