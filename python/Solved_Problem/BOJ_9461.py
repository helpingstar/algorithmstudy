import sys

input = sys.stdin.readline

t = int(input())
nums = []

for _ in range(t):
    nums.append(int(input()))

max_nums = max(nums)

tri = [0, 1, 1, 1, 2, 2, 3, 4, 5]

cnt = 8

while len(tri) <= max_nums:
    tri.append(tri[cnt] + tri[cnt-4])
    cnt += 1

for i in nums:
    print(tri[i])