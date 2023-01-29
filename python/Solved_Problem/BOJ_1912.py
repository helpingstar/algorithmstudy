import sys


input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

max_num = -1001
max_ans = 0
temp = 0
for i in range(n):
    if temp + nums[i] < 0:
        temp = 0
    else:
        temp += nums[i]
    max_ans = max(max_ans, temp)
    max_num = max(max_num, nums[i])

if max_ans == 0:
    print(max_num)
else:
    print(max_ans)
