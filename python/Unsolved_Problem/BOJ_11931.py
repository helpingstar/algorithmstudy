import sys

n = int(input())

nums = [int(input()) for _ in range(n)]

print(*reversed(sorted(nums)), sep='\n')
