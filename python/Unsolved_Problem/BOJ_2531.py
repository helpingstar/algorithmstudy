import sys
read = sys.stdin.readline
n, d, k, c = map(int, read().split())
arr = [int(read()) for _ in range(n)]
l = [0] * (d+1)
l[c] += 1
tmp = 1
for i in range(k):
    if l[arr[i]] < 1:
        tmp += 1
    l[arr[i]] += 1
ans = tmp
for ran in [range(k, n), range(k-1)]:
    for i in ran:
        l[arr[i-k]] -= 1
        if l[arr[i-k]] < 1:
            tmp -= 1
        l[arr[i]] += 1
        if l[arr[i]] < 2:
            tmp += 1
        ans = max(ans, tmp)
print(ans)