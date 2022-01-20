import sys
input = sys.stdin.readline

n = int(input())

max_t = [0] * 3
min_t = [0] * 3
for _ in range(n):
    line = list(map(int, input().split()))
    max_t[0], max_t[1], max_t[2] = max(max_t[0], max_t[1]) + line[0], max(max_t) + line[1], max(max_t[1], max_t[2]) + line[2]
    min_t[0], min_t[1], min_t[2] = min(min_t[0], min_t[1]) + line[0], min(min_t) + line[1], min(min_t[1], min_t[2]) + line[2]
print(max(max_t), min(min_t))