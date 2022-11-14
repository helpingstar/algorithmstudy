import sys

input = sys.stdin.readline

cache = dict()

def get_num(x) -> int:
    if x in cache:
        return cache[x]

    n = 1
    while True:
        if x <= (n*(n+1)):
            break
        n += 1
    if x <= n*n:
        ans = n*2 -1
    else:
        ans = n*2
    cache[x] = ans
    return ans

def solution():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(get_num(b - a))

solution()
