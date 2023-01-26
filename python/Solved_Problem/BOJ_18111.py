import sys
from collections import defaultdict

input = sys.stdin.readline

n, m, budget = map(int, input().split())
dic = defaultdict(int)

h_top, h_bottom = 0, 1000

for _ in range(n):
    line = list(map(int, input().split()))
    for num in line:
        dic[num] += 1
        h_top = max(h_top, num)
        h_bottom = min(h_bottom, num)
# area = n * m
n_top = dic[h_top]
n_bottom = dic[h_bottom]

time = 0
while h_bottom < h_top:
    if n_bottom <= 2 * n_top and n_bottom <= budget:
        budget -= n_bottom
        time += n_bottom

        h_bottom += 1
        if h_bottom in dic:
            n_bottom += dic[h_bottom]
    else:
        budget += n_top
        time += 2 * n_top

        h_top -= 1
        if h_top in dic:
            n_top += dic[h_top]

print(time, h_top)
