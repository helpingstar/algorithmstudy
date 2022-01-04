from collections import deque
import sys

n, m, v = map(int, sys.stdin.readline().rstrip().split())

node = {}


for i in range(1, n+1):
    node[i] = set()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    node[a].add(b)
    node[b].add(a)

