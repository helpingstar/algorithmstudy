import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
dic = defaultdict(int)
arr = list(map(int, input().split()))
ans = 0
prev = 0

for i in range(n):
    prev += arr[i]
    dic[prev % m] += 1

ans += dic[0]

for i in range(m):
    ans += dic[i] * (dic[i] - 1) // 2

print(ans)
