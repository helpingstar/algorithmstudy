import sys

input = sys.stdin.readline

n_wood, length = map(int, input().split())
heights = list(map(int, input().split()))

left, right = 0, 1000000000

while left <= right:
    mid = (left + right) // 2
    sum = 0
    for h in heights:
        sum += h - mid if h > mid else 0
    if sum >= length:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
