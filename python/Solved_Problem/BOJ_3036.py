import sys
import math

input = sys.stdin.readline

n = map(int, input().split())

nums = list(map(int, input().split()))

for num in nums[1:]:
    gcd = math.gcd(nums[0], num)
    print(f'{nums[0]//gcd}/{num//gcd}')
