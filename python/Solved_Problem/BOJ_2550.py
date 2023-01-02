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
cp = [0] * n_bulb

for i, l_num in enumerate(left):
    pos = bisect.bisect_left(dp, right_to_index[l_num])
    if pos == len(dp):
        dp.append(right_to_index[l_num])
    else:
        dp[pos] = right_to_index[l_num]

    cp[i] = pos

print(len(dp))
ans = []
cur = len(dp) - 1
for i in range(len(cp)-1, -1, -1):
    if cp[i] == cur:
        ans.append(left[i])
        cur -= 1
print(*sorted(ans))
