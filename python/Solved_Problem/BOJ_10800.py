import sys
from collections import defaultdict
import bisect

input = sys.stdin.readline

n = int(input())

d_dict = defaultdict(list)
sum_d_dict = defaultdict(list)
total = []
sum_total = []
input_list = []

for _ in range(n):
    a, b = map(int, input().split())
    d_dict[a].append(b)
    total.append(b)
    input_list.append((a, b))

for i in d_dict:
    d_dict[i].sort()
    temp = 0
    for c in d_dict[i]:
        temp += c
        sum_d_dict[i].append(temp)

total.sort()
temp = 0
for c in total:
    temp += c
    sum_total.append(temp)

for x, y in input_list:
    one_sum_idx = bisect.bisect_left(d_dict[x], y)
    all_sum_idx = bisect.bisect_left(total, y)
    print(sum_total[all_sum_idx] - sum_d_dict[x][one_sum_idx])