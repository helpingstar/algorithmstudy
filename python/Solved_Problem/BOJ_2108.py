import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

nums = []
count = defaultdict(int)

for _ in range(n):
    num = int(input())
    nums.append(num)
    count[num] += 1

nums.sort()
count_list = list(count.items())
count_list.sort(key=lambda x: (-x[1], x[0]))
tmp = sum(nums)/n

if -0.5 < tmp <= 0:
    print(0)
else:
    print(f'{tmp:.0f}')

print(nums[n//2])
if len(count_list) > 1 and count_list[0][1] == count_list[1][1]:
    print(count_list[1][0])
else:
    print(count_list[0][0])
print(nums[-1] - nums[0])
