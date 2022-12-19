import sys
import bisect
input = sys.stdin.readline

n_bulb = int(input())

left = list(map(int, input().split()))
right = list(map(int, input().split()))

right_to_index = [-1] * (n_bulb + 1)
for i, num in enumerate(right):
    right_to_index[num] = i

dp = []
num_pos = []

for i in left:
    pos = bisect.bisect_left(dp, right_to_index[i])
    if pos == len(dp):
        dp.append(right_to_index[i])
        num_pos.append(i)
    else:
        dp[pos] = right_to_index[i]
        if pos == len(dp) - 1:
            num_pos[pos] = i

print(len(dp))
print(*sorted(num_pos))
