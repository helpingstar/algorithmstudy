import sys

input = sys.stdin.readline

n, k = map(int ,input().split())
coins = []
ans = 0

for _ in range(n):
    coins.append(int(input()))

cur = n-1

while k > 0:
    temp = k // coins[cur]
    if temp > 0:
        ans += temp
        k %= coins[cur]
    cur -= 1

print(ans)
