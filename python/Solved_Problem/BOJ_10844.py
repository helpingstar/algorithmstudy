import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    for _ in range(n-1):
        new_dp = [0] * 10
        for i in range(10):
            if i > 0:
                new_dp[i-1] += dp[i]
            if i < 9:
                new_dp[i+1] += dp[i]
        for i in range(10):
            new_dp[i] %= 1000000000
    
        dp = new_dp
    return sum(dp) % 1000000000

print(solution())