import sys

input = sys.stdin.readline

n_card = int(input())

cards = [0] + list(map(int, input().split()))
dp = cards[:]
for i in range(2, n_card+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[j] + cards[i-j])

print(dp[n_card])
