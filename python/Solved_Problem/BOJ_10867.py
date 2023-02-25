import sys

input = sys.stdin.readline

n = int(input())

nums = set(map(int, input().split()))

print(*sorted(nums))