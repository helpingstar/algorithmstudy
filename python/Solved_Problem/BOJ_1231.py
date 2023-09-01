import sys


def solution():
    input = sys.stdin.readline

    n_stock, n_day, budget = map(int, input().split())

    price = [list(map(int, input().split())) for _ in range(n_stock)]

    for d in range(1, n_day):
        delta = [0] * (budget + 1)
        for s in range(n_stock):
            before = price[s][d - 1]
            after = price[s][d]
            for i in range(before, budget + 1):
                delta[i] = max(delta[i], delta[i - before] + after - before)
        # print(delta)
        budget += delta[budget]

    print(budget)


solution()
