import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

arr = []
time_dic = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    time_dic[a] += 1
    time_dic[b] -= 1

count = 0
max_count = 0
for key in sorted(time_dic.keys()):
    count += time_dic[key]
    if max_count < count:
        max_count = count

print(max_count)