import sys


def solution():
    input = sys.stdin.readline

    n_dish, kind_sushi, combo_dish, coupon = map(int, input().split())
    sushis = [int(input()) for _ in range(n_dish)]

    answer = 0

    eat_table = [0] * (kind_sushi + 1)
    eat_count = 0
    for i in range(combo_dish - 1):
        if eat_table[sushis[i]] == 0:
            eat_count += 1
        eat_table[sushis[i]] += 1

    for i in range(n_dish):
        if eat_table[sushis[(i + combo_dish - 1) % n_dish]] == 0:
            eat_count += 1
        eat_table[sushis[(i + combo_dish - 1) % n_dish]] += 1
        # print("debug", (i + combo_dish) % n_dish, eat_count)
        # print(eat_table)
        answer = max(answer, eat_count + 1 if eat_table[coupon] == 0 else eat_count)

        if eat_table[sushis[i]] == 1:
            eat_count -= 1
        eat_table[sushis[i]] -= 1

    print(answer)


solution()

"""
8 30 4 30
9
25
7
9
7
30
2
7
"""
