import sys
import bisect

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
sums = [0] * (N+1)
for i in range(N):
    sums[i+1] = sums[i] + nums[i]

l, r = 0, nums[-1]

budget = int(input())

# print(f'[debug] nums: {nums}')
# print(f'[debug] sums: {sums}')

while l <= r:
    mid = (l + r) // 2

    pos = bisect.bisect_left(nums, mid)
    result = sums[pos]

    result += (N-pos) * mid
    # print(f'[debug]  mid: {mid}, pos: {pos}, result: {result}')
    if result <= budget:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)
