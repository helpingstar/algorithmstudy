"""
회전은 큐다 배열의 복사만 하다가 시간초과가 났다.
회전은 큐다
"""

import sys
from collections import deque
input = sys.stdin.readline

a, b, d, N = map(int, input().split())

table = deque([1] + ([0] * (d-1)))

adult = 0

for _ in range(N):
    temp = [0]
    table.pop()

    
    adult = (adult + table[a-1] - table[b-1]) % 1000
    table.appendleft(adult)

print(sum(table) % 1000)