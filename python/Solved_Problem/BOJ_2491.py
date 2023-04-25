import sys

input = sys.stdin.readline

up = 1
down = 1

N = int(input())
ans = 1
nums = list(map(int, input().split()))

for i in range(N-1):
    if nums[i] == nums[i+1]:
        up += 1
        down += 1
    elif nums[i] < nums[i+1]:
        up += 1
        ans = max(ans, down)
        down = 1
    else:
        down += 1
        ans = max(ans, up)
        up = 1

ans = max(ans, up, down)
print(ans)
