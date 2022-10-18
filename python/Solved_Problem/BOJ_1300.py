import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

l, r = 1, n*n
ans = 0
while l <= r:
    mid = l + (r-l) // 2
    temp = 0
    for i in range(1, n+1):
        temp += min(n, mid // i)
    if k <= temp:
        ans = mid
        r = mid-1
    else:
        l = mid+1

print(ans)
