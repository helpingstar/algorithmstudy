import sys

input = sys.stdin.readline

d = int(input())
dp = [0] * 8
dp[0] = 1
for _ in range(d):
    new_dp = [0] * 9
    new_dp[0] = (dp[1] + dp[2]) % 1000000007
    new_dp[1] = (dp[0] + dp[2] + dp[3]) % 1000000007
    new_dp[2] = (dp[0] + dp[1] + dp[3] + dp[4]) % 1000000007
    new_dp[3] = (dp[1] + dp[2] + dp[4] + dp[5]) % 1000000007
    new_dp[4] = (dp[2] + dp[3] + dp[5] + dp[7]) % 1000000007
    new_dp[5] = (dp[3] + dp[4] + dp[6]) % 1000000007
    new_dp[6] = (dp[5] + dp[7]) % 1000000007
    new_dp[7] = (dp[4] + dp[6]) % 1000000007
    
    dp = new_dp

print(dp[0])