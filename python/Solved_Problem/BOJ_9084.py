import sys

input = sys.stdin.readline

def solution():
    n_coin = int(input())
    coins = list(map(int, input().split()))
    target = int(input())

    dp = [0] * (target + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, target+1):
            dp[i] += dp[i - coin]
    # print(dp)
    print(dp[target])
for _ in range(int(input())):
    solution()
