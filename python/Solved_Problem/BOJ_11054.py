import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left_start = [0] * n
right_start = [0] * n

left_dp = []
right_dp = []

for idx, num in enumerate(arr):
    pos = bisect.bisect_left(left_dp, num)
    if pos == len(left_dp):
        left_dp.append(num)
    else:
        left_dp[pos] = num
    left_start[idx] = pos

for idx, num in enumerate(arr[::-1]):
    pos = bisect.bisect_left(right_dp, num)
    if pos == len(right_dp):
        right_dp.append(num)
    else:
        right_dp[pos] = num
    right_start[idx] = pos

# print(f'[debug]  left_start: {left_start}')
# print(f'[debug]  right_start: {right_start}')
# print(f'[debug]  left_dp: {left_dp}')
# print(f'[debug]  right_dp: {right_dp}')


ans = 0
for i in range(n):
    ans = max(ans, left_start[i] + right_start[n-1-i])
print(ans+1)
