import sys


def solution():
    input = sys.stdin.readline
    N = int(input())

    waters = [int(input()) for _ in range(N)]

    if N == 1:
        return waters[0]
    elif N == 2:
        return sum(waters)
    elif N == 3:
        return sum(waters) - min(waters)

    dp = [waters[0]+waters[1], waters[0]+waters[2], waters[1]+waters[2]]
    for i in range(3, N):
        a = max(dp)
        b = dp[0] + waters[i]
        c = dp[1] + waters[i]
        dp = [a, b, c]
    return max(dp)


print(solution())
