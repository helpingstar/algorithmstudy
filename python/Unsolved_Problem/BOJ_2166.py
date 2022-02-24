import sys

input = sys.stdin.readline

n = int(input())

a1, b1 = map(int, input().split())
a, b = a1, b1
result = 0

for _ in range(n-1):
    c, d = map(int, input().split())
    result += a * d
    result -= b * c
    a, b = c, d

result += c*b1
result -= d*a1

result = abs(result)
result *= 0.5

print(f'{result:.1f}')