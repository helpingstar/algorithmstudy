import sys
from itertools import combinations
import bisect

input = sys.stdin.readline

N, target = map(int, input().split())

nums = list(map(int, input().split()))

list1 = nums[:N//2]
list2 = nums[N//2:]

comb1 = []

for i in range(len(list1)+1):
    for comb in combinations(list1, i):
        comb1.append(sum(comb))

comb1.sort()

answer = 0

for i in range(len(list2)+1):
    for comb in combinations(list2, i):
        temp = sum(comb)
        temp = target - temp
        answer += bisect.bisect_right(comb1, temp)
# print(f'[debug]  list1: {list1}')
# print(f'[debug]  list2: {list2}')
# print(comb1)
print(answer)
