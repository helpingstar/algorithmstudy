import sys

input = sys.stdin.readline

N = int(input())
target = int(input())

pieces = list(map(int, input().split()))

pieces.sort()

l, r = 0, N-1
ans = 0

while l < r:
    temp = pieces[l] + pieces[r]
    if temp < target:
        l += 1
    elif temp > target:
        r -= 1
    else:
        ans += 1
        l += 1
        r -= 1

print(ans)
