import sys

input = sys.stdin.readline
INF = int(1e7)
n, target = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]

for i in range(n):
    sums.append(sums[-1] + nums[i])

left, right = 0, 0
ans = INF
# print(sums)

while left <= right and right <= n:
    
    temp = sums[right] - sums[left]
    if temp < target:
        right += 1
    else:
        ans = min(ans, right - left)
        left += 1
        
if ans == INF:
    print(0)
else:
    print(ans)