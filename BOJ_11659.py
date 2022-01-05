import sys

n, m = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

num_sum = [0] * (n + 1)
num_sum[1] = num[0]

for i in range(1, 5):
    num_sum[i+1] = num[i] + num_sum[i]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(num_sum[b] - num_sum[a-1])