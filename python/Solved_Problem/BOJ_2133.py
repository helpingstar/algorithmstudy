
def solution():
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    if n == 2:
        return 3
    for i in range(2, n+1, 2):
        dp[i] += 3 * dp[i-2]
        dp[i] += 2 * sum(dp[:i-2])
    return dp[n]

print(solution())
