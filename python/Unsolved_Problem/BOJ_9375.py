import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    dic = defaultdict(int)
    for _ in range(n):
        clothes, kind = input().split()
        dic[kind] += 1
    n_clothes = list(dic.values())
    result = 0
    for n_select in range(1, len(n_clothes)+1):
        combs = combinations(n_clothes, n_select)
        for comb in combs:
            temp = 1
            for i in comb:
                temp *= i
            result += temp
    print(result)
