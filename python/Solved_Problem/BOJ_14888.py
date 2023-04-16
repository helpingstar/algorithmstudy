import sys
from itertools import permutations

input = sys.stdin.readline

INF = 30_0000_0000

cal_map = ['+', '-', '*', '/']

N = int(input())
nums = list(map(int, input().split()))
cals = list(map(int, input().split()))

all_cals = []

for i, cal in enumerate(cal_map):
    all_cals += [cal] * cals[i]

def operation(n1, n2, oper):
    if oper == '+':
        return n1 + n2
    elif oper == '-':
        return n1 - n2
    elif oper == '*':
        return n1 * n2
    else:
        return int(n1 / n2)

min_ans = INF
max_ans = -INF

for comb in permutations(all_cals, N-1):
    # print(comb)
    temp = nums[0]
    for i, c in enumerate(comb):
        temp = operation(temp, nums[i+1], c)
    min_ans = min(min_ans, temp)
    max_ans = max(max_ans, temp)

print(max_ans)
print(min_ans)
