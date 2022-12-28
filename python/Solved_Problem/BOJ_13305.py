import sys

input = sys.stdin.readline

n_city = int(input())

costs = list(map(int, input().split()))

prices = list(map(int, input().split()))

min_price = sys.maxsize

ans = 0
for i in range(n_city-1):
    min_price = min(min_price, prices[i])
    ans += min_price * costs[i]

print(ans)
