import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

l, r = 1, k
result = 0

while l <= r:
    mid = (l + r) // 2

    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, mid // i)
    
    # cnt 가 k보다 큰 것은 답의 가능성을 가진다
    if cnt >= k:
        result = mid
        r = mid - 1
    else:
        l = mid + 1

print(result)