import sys

input = sys.stdin.readline

n = int(input())
papers = []
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        papers.append((a, b))
    else:
        papers.append((b, a))
