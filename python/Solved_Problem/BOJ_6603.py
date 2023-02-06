import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    while True:
        inp = list(map(int, input().split()))
        if inp[0] == 0:
            return

        for comb in combinations(inp[1:], 6):
            print(*comb)
        print()


solution()
    