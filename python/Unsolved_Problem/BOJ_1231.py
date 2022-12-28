import sys

input = sys.stdin.readline

n_stock, n_day, budget = map(int, input().split())

price = [list(map(int, input().split())) for _ in range(n_stock)]

for d in range(n_day-1):
    profit = 0
    for s in range(n_stock):
        profit = max(profit, budget // price[s][d] * (price[s][d+1] - price[s][d]))
    budget += profit

print(budget)
