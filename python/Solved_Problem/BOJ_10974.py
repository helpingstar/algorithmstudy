import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

permuts = permutations(range(1, n+1), n)

for permut in permuts:
    print(*permut)