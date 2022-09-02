import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

left = 1
right = n*n

answer = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in range(1, n+1):
        total += min(n, mid//i)

    if k <= total:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)