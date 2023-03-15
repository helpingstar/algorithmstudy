import sys

input = sys.stdin.readline

cache = dict()


def rec(a, b, c):
    if (a, b, c) in cache:
        return cache[(a, b, c)]
    if a <= 0 or b <= 0 or c <= 0:
        cache[(a, b, c)] = 1
        return 1
    elif a > 20 or b > 20 or c > 20:
        cache[(a, b, c)] = rec(20, 20, 20)
        return cache[(a, b, c)]
    elif a < b < c:
        cache[(a, b, c)] = rec(a, b, c-1) + rec(a, b-1, c-1) - rec(a, b-1, c)
        return cache[(a, b, c)]
    else:
        cache[(a, b, c)] = rec(a-1, b, c) + rec(a-1, b-1, c) + \
            rec(a-1, b, c-1) - rec(a-1, b-1, c-1)
        return cache[(a, b, c)]


while True:
    a, b, c = map(int, input().split())

    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {rec(a, b, c)}')
