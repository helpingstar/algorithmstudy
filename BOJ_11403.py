import sys
import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
node = defaultdict(list)

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if line[j] == 1:
            node[i].append(j)

def bfs(x):
    