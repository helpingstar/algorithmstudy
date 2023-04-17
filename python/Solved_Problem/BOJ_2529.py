import sys
from itertools import permutations

input = sys.stdin.readline

K = int(input())

ineqs = list(input().split())

def check_ineq(a, eq, b):
    if eq == '<':
        if a < b:
            return True
        else:
            return False
    else:
        if a > b:
            return True
        else:
            return False

def check_perm(perm):
    global K
    global ineqs
    for i in range(K):
        if not check_ineq(perm[i], ineqs[i], perm[i+1]):
            return False
    return True

ans_min = float('inf')
ans_max = -float('inf')

for perm in permutations(range(10), K+1):
    if check_perm(perm):
        # print('hiroo')
        ans_min = min(ans_min, int(''.join(map(str, perm))))
        ans_max = max(ans_max, int(''.join(map(str, perm))))

print('0'*(1+K-len(str(ans_max))), ans_max, sep='')
print('0'*(1+K-len(str(ans_min))), ans_min, sep='')
