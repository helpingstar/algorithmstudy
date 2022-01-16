import sys
input = sys.stdin.readline

n = int(input())

node = [[] for _ in range(n)]

for i in range(n):
    num_list = list(map(int, input().split()))
    for j in range(n):
        if num_list[j] == 1:
            node[i].append(j)

