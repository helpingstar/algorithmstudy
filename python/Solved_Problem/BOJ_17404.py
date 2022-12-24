import sys

input = sys.stdin.readline
INF = 1000000
n = int(input())

first_line = list(map(int, input().split()))

l = first_line[:]
l[0] = INF
c = first_line[:]
c[1] = INF
r = first_line[:]
r[2] = INF

for _ in range(n-2):
    line = list(map(int, input().split()))
    for li in [l, c, r]:
        li[0], li[1], li[2] = min(li[1:]) + line[0], min(li[0], li[2]) + line[1], min(li[:2]) + line[2]
    # print(l, c, r)

result = []

line = list(map(int, input().split()))

result.append(min(l[1:]) + line[0])
result.append(min(c[0], c[2]) + line[1])
result.append(min(r[:2]) + line[2])

print(min(result))