import sys

input = sys.stdin.readline

n = int(input())

sum = 0
i = 1

while sum < n:
    sum += i
    i += 1

if sum == n:
    print(i-1)
else:
    print(i-2)
