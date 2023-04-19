import sys

input = sys.stdin.readline

F = int(input())

nums = []

R = 0
C = 0

for i in range(6):
    a, b = map(int, input().split())
    nums.append((a, b))
    if a in {4, 3}:
        R = max(R, b)
    else:
        C = max(C, b)

ans = R * C

target = {(2, 4), (3, 2), (1, 3), (4, 1)}

for i in range(6):
    if (nums[i-1][0], nums[i][0]) in target:
        print(F * (ans - nums[i-1][1]*nums[i][1]))
        break
