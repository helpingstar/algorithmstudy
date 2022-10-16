import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

arr = input().rstrip()
dp = [0 for _ in range(m)]
last = []
prev = 0
for i in range(2, m):
    if arr[i] == 'I':
        if arr[i - 2] == 'I' and arr[i-1] == 'O':
            dp[i] = dp[i-2] + 1
            prev = dp[i]
        else:
            last.append(prev)
            prev = 0
last.append(prev)

ans = 0

for i in last:
    ans += max(0, i - (n-1))

print(ans)
