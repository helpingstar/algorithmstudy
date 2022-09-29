import sys

input = sys.stdin.readline

n = int(input())
board = set(map(int, input().split()))

m = int(input())

nums = list(map(int, input().split()))

for num in nums:
    if num in board:
        print(1)
    else:
        print(0)
