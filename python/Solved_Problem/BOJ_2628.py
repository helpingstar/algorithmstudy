import sys


input = sys.stdin.readline

C, R = map(int, input().split())

rows = [0, R]
cols = [0, C]

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    if a == 0:
        rows.append(b)
    else:
        cols.append(b)

rows.sort()
cols.sort()

r_max = 0
c_max = 0

for i in range(1, len(rows)):
    r_max = max(r_max, rows[i] - rows[i-1])

for i in range(1, len(cols)):
    c_max = max(c_max, cols[i] - cols[i-1])

print(r_max * c_max)
