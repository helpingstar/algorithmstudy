import sys
import heapq

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

work = [c] * (n+1)
result = 0
w_list = []

for i in range(1, m+1):
    a, b, w = map(int, input().split())
    w_list.append((b, a, w))

w_list.sort()

for b, a, w in w_list:
    w_min = min(min(work[a:b]), w)
    if w_min == 0:
        continue
    for i in range(a, b):
        work[i] -= w_min
    result += w_min
    
print(result)