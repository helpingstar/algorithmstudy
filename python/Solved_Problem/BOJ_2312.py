import sys
from collections import defaultdict
input = sys.stdin.readline


def solution():
    N = int(input())
    ans = defaultdict(int)
    i = 2
    while N > 1:
        while N % i == 0:
            ans[i] += 1
            N //= i
        if N == 1:
            break
        i += 1
    for k in sorted(ans.keys()):
        print(k, ans[k])


T = int(input())

for _ in range(T):
    solution()
