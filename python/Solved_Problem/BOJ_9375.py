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
    result = 1
    for num in dic.values():
        result *= (num+1)
    print(result-1)
