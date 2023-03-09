import sys

input = sys.stdin.readline

n = int(input())

nums = [int(input()) for _ in range(n)]

nums.sort()

max_num = nums[-2]
ans = []
for i in range(2, max_num+1):
    flag = True
    for num in nums:
        if num % i != nums[0] % i:
            flag = False
            break
    if flag:
        ans.append(i)

print(*ans)
