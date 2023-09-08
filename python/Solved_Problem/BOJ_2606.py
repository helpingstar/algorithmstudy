import sys

input = sys.stdin.readline


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    n_pc = int(input())
    n_con = int(input())

    parent = [i for i in range(n_pc + 1)]

    for _ in range(n_con):
        a, b = map(int, input().split())

        union(parent, a, b)
    result = 0
    for i in range(2, n_pc+1):
        if find(parent, i) == 1:
            result += 1

    print(result)


solution()
