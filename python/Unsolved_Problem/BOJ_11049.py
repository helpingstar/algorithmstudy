import sys
import heapq
input = sys.stdin.readline

n = int(input().split())

visited = [False] * n

q = []
matrix_list = []

for _ in range(n):
    a, b = map(int, input().split())
    matrix_list.append((a, b))

for i in range(n-1):
    a, b = matrix_list[i]
    _, c = matrix_list[i+1]
    
    cost = a * b * c
    
    heapq.heappush(q, (cost, i, i+1))
    
result = 0

while q:
    cost, i, j = heapq.heappop(q)
    result += cost
    visited[i] = True
    visited[j] = True
    heapq.heappush(q, ())