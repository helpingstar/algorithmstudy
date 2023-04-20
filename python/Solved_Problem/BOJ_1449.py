import sys

input = sys.stdin.readline

N, L = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

temp = 0
ans = 0
for num in nums:
    if num > temp:
        temp = num + L - 1
        ans += 1

print(ans)
