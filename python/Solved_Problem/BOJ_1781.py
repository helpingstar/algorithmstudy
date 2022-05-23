"""
문제의 개수n부터 1까지 for문을 돌면서
각 문제의 deadline이 커서인 i보다 작은것들(같은 것으로 해도 됨)의 컵라면 수를
max heapq에 저장한다. 그리고 1 loop당 heapq안에 요소가 있을 경우 하나씩 pop해서 reuslt에 더한다.

"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())
problems = []

for _ in range(n):
    dead, cup = map(int, input().split())
    problems.append((dead, cup))

problems.sort()
q = []
result = 0

for i in range(n, 0, -1):
    while problems and problems[-1][0] >= i:
        heapq.heappush(q, -problems.pop()[1])
    if q:
        result += -heapq.heappop(q)

print(result)