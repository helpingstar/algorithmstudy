import sys
from itertools import combinations

input = sys.stdin.readline

T = int(input())

def solution():
    n = int(input())
    vec_list = []
    total_x = total_y = 0
    for _ in range(n):
        a, b = map(int, input().split())
        total_x += a
        total_y += b
        vec_list.append((a, b))

    combis = list(combinations(vec_list, n//2))
    answer = sys.maxsize
    for comb in combis:
        temp_x = temp_y = 0
        for x, y in comb:
            temp_x += x
            temp_y += y
        v_x, v_y = total_x - temp_x, total_y - temp_y
        answer = min(answer, ((v_x-temp_x) ** 2 + (v_y-temp_y) ** 2) ** 0.5)
    return answer

for _ in range(T):
    print(solution())
