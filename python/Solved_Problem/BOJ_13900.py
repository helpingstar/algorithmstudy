import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
sum = [0] * n
cur = 0
for i in range(n-1):
    cur += nums[-(1+i)]
    sum[-(2+i)] = cur

total = 0

for i in range(n-1):
    total += nums[i] * sum[i]

print(total)