import sys
import math

input = sys.stdin.readline

N = int(input())

nums = [int(input()) for _ in range(N)]

nums.sort()

nums2 = []

for i in range(N-1):
    nums2.append(nums[i+1] - nums[i])

gcd = nums2[0]

for i in range(1, N-1):
    gcd = math.gcd(gcd, nums2[i])

result = [gcd]

for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        if i * i != gcd:
            result.append(i)
            result.append(gcd // i)
        else:
            result.append(i)

result.sort()
print(*result, sep='\n')
