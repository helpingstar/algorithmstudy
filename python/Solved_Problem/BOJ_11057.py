import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    dp = [1] * 10
    for _ in range(n-1):
        new_dp = [0] * 10
        for i in range(10):
            for j in range(i, 10):
                new_dp[j] += dp[i]
        dp = new_dp
    
    return sum(dp) % 10007

print(solution())
    