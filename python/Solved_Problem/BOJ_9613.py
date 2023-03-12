import sys
import math
input = sys.stdin.readline

for _ in range(int(input())):
    ans = 0
    nums = list(map(int, input().split()))
    N = nums[0]
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            ans += math.gcd(nums[i], nums[j])
    print(ans)
