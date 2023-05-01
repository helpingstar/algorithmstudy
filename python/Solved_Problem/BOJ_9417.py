import sys
import math

input = sys.stdin.readline

for _ in range(int(input())):
    nums = list(map(int, input().split()))

    ans = 1

    for i in range(len(nums)):
        for j in range(i):
            ans = max(ans, math.gcd(nums[i], nums[j]))

    print(ans)
