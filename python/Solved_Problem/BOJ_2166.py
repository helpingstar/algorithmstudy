import sys

input = sys.stdin.readline

n = int(input())

total = 0
a, b = map(int, input().split())
ac, bc = a, b
for _ in range(n-1):
    c, d = map(int, input().split())
    total += a * d
    total -= b * c
    a, b = c, d

total += c * bc
total -= d * ac

total *= 0.5
total = abs(total)

print(f'{total:.1f}')