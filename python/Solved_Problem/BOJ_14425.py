import sys

input = sys.stdin.readline

n, m = map(int, input().split())

strings = set()

for _ in range(n):
    strings.add(input().rstrip())
ans = 0
for _ in range(m):
    temp = input().rstrip()
    
    if temp in strings:
        ans += 1

print(ans)