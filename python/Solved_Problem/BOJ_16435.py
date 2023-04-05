import sys

input = sys.stdin.readline

N, length = map(int, input().split())

nums = list(map(int, input().split()))

nums.sort()

for num in nums:
    if num <= length:
        length += 1

print(length)
