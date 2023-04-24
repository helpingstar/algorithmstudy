import sys

input = sys.stdin.readline
INF = int(1e6)
N = int(input())

prices = [0] + list(map(int, input().split()))

values = [INF] * (N+1)
values[0] = 0

for i in range(1, N+1):
    for j in range(i):
        values[i] = min(values[i], prices[i-j] + values[j])

print(values[-1])
