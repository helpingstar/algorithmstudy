import sys
input = sys.stdin.readline

n = int(input())

value = set()

for _ in range(n):
    a, b = map(int, input().split())
    for r in range(10):
        for c in range(10):
            value.add((a+r, b+c))

print(len(value))