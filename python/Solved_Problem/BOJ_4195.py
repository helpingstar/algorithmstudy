import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b, relations:defaultdict):
    a = find(parent, a)
    b = find(parent, b)

    a_r = relations[a]
    b_r = relations[b]

    if a > b:
        parent[a] = b
        relations[b] += relations[a]
    else:
        parent[b] = a
        relations[a] += relations[b]

def solution():
    n_edge = int(input())
    relations = defaultdict(lambda: 1)
    parent = dict()
    for _ in range(n_edge):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
        if b not in parent:
            parent[b] = b
        if find(parent, a) != find(parent, b):
            union(parent, a, b, relations)
            print(relations[find(parent, a)])
        else:
            print(relations[find(parent, a)])



for _ in range(T):
    solution()
