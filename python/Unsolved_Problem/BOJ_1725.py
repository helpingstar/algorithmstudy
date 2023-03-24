import sys

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]
dp = []
ans = 0
for i, num in enumerate(nums):
    if dp:
        while dp and dp[-1] > num:
            temp = dp.pop()

    dp.append(num)
    print(dp)

print(ans)
