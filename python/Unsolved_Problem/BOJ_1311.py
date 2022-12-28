import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

price = []

for _ in range(n):
    line = list(map(int, input().split()))
    price.append(line)

ans = sys.maxsize
for perm in permutations(range(n), n):
    temp = 0
    for i, num in enumerate(perm):
        temp += price[i][num]
    ans = min(ans, temp)

print(ans)
