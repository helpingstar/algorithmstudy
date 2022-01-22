import sys
import bisect
from collections import defaultdict
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
table = []
for i in range(len(s2)):
    update = defaultdict(list)
    for j in range(len(s1)):
        if s2[i] == s1[j]:
            pos = bisect.bisect_left(table, j)
            update[pos].append(j)
            
    for i in update:
        if len(table) <= i:
            table.append(min(update[i]))
        else:
            table[i] = min(update[i])

print(len(table))