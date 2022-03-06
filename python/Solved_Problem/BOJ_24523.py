import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

result = []
prev = li[0]
count = 1
for i in range(1, n):
    if prev == li[i]:
        count += 1
    else:
        for _ in range(count):
            result.append(i+1)
        count = 1
        
    prev = li[i]

for _ in range(count):
    result.append(-1)

print(*result)