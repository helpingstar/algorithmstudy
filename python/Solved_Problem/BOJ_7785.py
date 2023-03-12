import sys

input = sys.stdin.readline

N = int(input())

company = set()

for _ in range(N):
    a, b = input().split()

    if b == 'enter':
        company.add(a)
    else:
        company.remove(a)

print(*reversed(sorted(company)), sep='\n')
