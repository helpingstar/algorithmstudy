import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

dp = [0] * (len(a) - len(b) + 1)
ans = 0

for i in range(len(a) - len(b) + 2):
    if a[i:i+len(b)] == b:
        if i >= len(b):
            dp[i] = max(dp[:i-len(b)+1]) + 1
        else:
            dp[i] = 1
        ans = max(dp[i], ans)

print(ans)
