import sys

input = sys.stdin.readline

N, target = map(int, input().split())

ranks = []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    ranks.append((b, c, d, a))

ranks.sort(key=lambda x: (-x[0], -x[1], -x[2]))

tr = 0

# print(ranks)

for i, rank in enumerate(ranks):
    if rank[-1] == target:
        tr = i
        break
# print(tr)
while ranks[tr-1][:-1] == ranks[tr][:-1]:
    tr -= 1

print(tr+1)
