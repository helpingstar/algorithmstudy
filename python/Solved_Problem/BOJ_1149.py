import sys

input = sys.stdin.readline

n = int(input())

rt, gt, bt = map(int, input().split())

for _ in range(n-1):
    r, g, b = map(int, input().split())
    rt, gt, bt = min(gt, bt) + r, min(rt, bt) + g, min(rt, gt) + b

print(min(rt, gt, bt))
    