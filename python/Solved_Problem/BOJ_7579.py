import sys


def solution():
    input = sys.stdin.readline

    n_app, target = map(int, input().split())
    memory = (0,) + tuple(map(int, input().split()))
    costs = (0,) + tuple(map(int, input().split()))

    col = sum(costs)
    result = float("inf")
    now = [0] * (col + 1)

    for r in range(1, n_app + 1):
        prev = now
        now = [0] * (col + 1)

        for c in range(col + 1):
            if c < costs[r]:
                now[c] = prev[c]
            else:
                now[c] = max(prev[c], prev[c - costs[r]] + memory[r])
                if now[c] >= target:
                    result = min(result, c)
        # print(now)
    print(result)


solution()
