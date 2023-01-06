import sys
from itertools import combinations
input = sys.stdin.readline

n_size, m = map(int, input().split())

board = []

house_list = []
chicken_list = []

for r in range(n_size):
    line = list(map(int, input().split()))
    for c, num in enumerate(line):
        if num == 1:
            house_list.append((r, c))
        elif num == 2:
            chicken_list.append((r, c))

chicken_combs = combinations(chicken_list, m)

answer = sys.maxsize
for chicken_comb in chicken_combs:
    temp_answer = 0
    for h_r, h_c in house_list:
        chicken_dist = sys.maxsize
        for c_r, c_c in chicken_comb:
            chicken_dist = min(chicken_dist, abs(h_r-c_r) + abs(h_c-c_c))
        temp_answer += chicken_dist
    answer = min(answer, temp_answer)

print(answer)
