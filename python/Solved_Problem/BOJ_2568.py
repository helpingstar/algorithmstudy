import sys
import bisect

input = sys.stdin.readline

n = int(input())

left, right = [], []
dp = []
cp = [0] * n

l2r_map = dict()
for _ in range(n):
    a, b = map(int, input().split())
    left.append(a)
    right.append(b)
    l2r_map[a] = b
left.sort()


for i, num in enumerate(left):
    pos = bisect.bisect_left(dp, l2r_map[num])
    if pos == len(dp):
        dp.append(l2r_map[num])
    else:
        dp[pos] = l2r_map[num]
    cp[i] = pos
result = []
cnt = len(dp) - 1
for i in range(n-1, -1, -1):
    if cnt == cp[i]:
        cnt -= 1
    else:
        result.append(left[i])

print(len(result))
print(*result[::-1], sep='\n')
