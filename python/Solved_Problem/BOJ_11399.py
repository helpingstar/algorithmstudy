import sys

n = int(sys.stdin.readline().rstrip())
line = list(map(int, sys.stdin.readline().split()))

line.sort()

total = 0
for i in range(n):
    total += line[i] * (n-i)

print(total)