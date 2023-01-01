import sys

input = sys.stdin.readline

n, k = map(int, input().split())

lines = [int(input()) for _ in range(n)]

lines.sort()

max_num = lines[-1]

l, r = 1, max_num

while l <= r:
    mid = (l+r) // 2
    result = 0
    for num in lines:
        result += num // mid

    if result >= k:
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)
