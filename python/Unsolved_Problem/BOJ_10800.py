import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = []
c_sumdict = defaultdict(int)
for _ in range(n):
    color, scale = map(int, input().split())
    c_sumdict[color] += scale
    arr.append(scale)

arr.sort()

sum_by_num = defaultdict(int)
for sc in arr:
    sum_by_num[sc] += 1

sum_list = defaultdict(int)
for k in sum_by_num.keys():
    sum_list